import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

def web_search(user_query):
    def search(user_query):
        url = "https://google.serper.dev/news"

        payload = json.dumps({
          "q": user_query
        })
        headers = {
          'X-API-KEY': os.environ["SERPER_API_KEY"],
          'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response.text

    def extract_links(json_result):
        links = []
        data = json.loads(json_result)

        for item in data.get('news', []):
            link = item.get('link')
            if link:
                links.append(link)

        return links[:5]

    json_result = search(user_query)

    if json_result:
        extracted_links = extract_links(json_result)
        return extracted_links
    else:
        print("Error in API request.")
        return None
