import json
import os
import sys

import requests
from dotenv import load_dotenv

sys.path.append(os.path.abspath("src"))

from models import llm, llm1

load_dotenv()

def quick_web_search(user_query):
    """
    Perform a web search using the Serper API.

    Parameters:
    - user_query (str): The user's query for the web search.

    Returns:
    - list or None: A list of the top 5 links extracted from the API response
                    if the request is successful, otherwise None.
    """

    # Set up the API endpoint URL
    url = "https://google.serper.dev/news"

    # Prepare the request payload with the user's query
    payload = json.dumps({
        "q": user_query
    })

    # Set up the request headers with the API key
    headers = {
        'X-API-KEY': os.environ["SERPER_API_KEY"],
        'Content-Type': 'application/json'
    }

    # Make a POST request to the API
    response = requests.request("POST", url, headers=headers, data=payload)

    # Check if the API request was successful
    if response.ok:
        # Extract links from the JSON response
        links = []
        data = json.loads(response.text)
        for item in data.get('news', []):
            link = item.get('link')
            if link:
                links.append(link)

        # Return the top 5 links
        return links[:3]
    else:
        # Handle the case where there's an error in the API request
        print(f"Error in API request. Status code: {response.status_code}")
        return None

def deep_web_search(user_query):
    prompt = """Write three Google search queries to gather information online \
        that helps form an objective opinion from the following topic: {}.\nYou \
        must strictly respond with a list of strings in the following \
        format:\n["Query 1", "Query 2", "Query 3"]""".format(user_query)

    result = llm1.invoke(prompt)
    
    if result:
        queries = json.loads(result)
        search_results = []

        for query in queries:
            # Perform a quick web search for each query
            links = quick_web_search(query)

            # Append the search results to the list
            search_results.append(f"'{query}':\n" + '\n'.join(links))

        # Print the concatenated search results
        final_result = '\n'.join(search_results)

        return final_result
    else:
        return "Error in generating search queries."