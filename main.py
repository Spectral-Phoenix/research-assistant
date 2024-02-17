import os
import time

from dotenv import load_dotenv
from langchain_community.llms import Cohere
from langchain_google_genai import ChatGoogleGenerativeAI

from scrape import scrape_text
from search import web_search

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

def summarise(user_query,text):
    prompt_template = f"Provide a detailed response to the following question based on the context provided.\nQuestion: {user_query}\nContext:\n{text}"

    result = llm1.invoke(prompt_template)

    return result

user_query = input("Enter the Query: ")

start_time = time.time()

# Search the Web and Collect Links
links = web_search(user_query)
print("Web Search Completed!")

# Scrape the Text from the Links
text = scrape_text(links)
answer = summarise(user_query, text)

end_time = time.time()
elapsed_time = "{:.2f}".format(end_time - start_time)

print(f"\nAnswer: {answer}")

print(f"Time Elapsed: {elapsed_time} seconds")