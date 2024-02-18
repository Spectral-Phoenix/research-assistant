import time
import streamlit as st

from src.scrape import scrape
from src.search import quick_web_search, deep_web_search
from src.summarise import summarise

st.title("Research Assistant")
user_query = st.text_input("Enter the Query: ")

start_time = time.time()

# Search the Web and Collect Links4
links = quick_web_search(user_query)
st.info("Web Search Completed!")

# Scrape the Text from the Links
text = scrape(links)
answer = summarise(user_query, text)

end_time = time.time()
elapsed_time = "{:.2f}".format(end_time - start_time)

st.markdown(f"\nAnswer: {answer}")

st.text(f"Time Elapsed: {elapsed_time} seconds")