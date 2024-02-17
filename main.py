import os
import time

from dotenv import load_dotenv
from langchain_community.llms import Cohere
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.environ["GEMINI_API_KEY"]
api_key_1 = os.environ["COHERE_API_KEY"]

llm = ChatGoogleGenerativeAI(model="gemini-pro",
                                google_api_key=api_key,
                                temperature = 0.5)

llm1 = Cohere(model="command-nightly",
                cohere_api_key = api_key_1,
                max_tokens=4096,
                temperature=0.5,)

def search(user_query):
    wrapper = DuckDuckGoSearchAPIWrapper(region="en-us",safesearch='off', time="d", max_results=10)
 
    search = DuckDuckGoSearchResults(api_wrapper=wrapper, source="news")
 
    text = search.run(user_query)

    return text

def summarise(user_query,web_search):
    prompt_template = f"Answer the following question based on the context provided.\nQuestion: {user_query}\nContext:\n{web_search}"

    result = llm1.invoke(prompt_template)

    return result

user_query = input("Enter the Query: ")

start_time = time.time()

web_search = search(user_query)

print("Web Search Completed!")

answer = summarise(user_query, web_search)

end_time = time.time()
elapsed_time = "{:.2f}".format(end_time - start_time)

print(f"\nAnswer: {answer}")

print(f"Time Elapsed: {elapsed_time} seconds")