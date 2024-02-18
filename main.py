import time

from src.scrape import scrape_text
from src.search import quick_web_search, deep_web_search
from src.summarise import summarise

user_query = input("Enter the Query: ")

start_time = time.time()

# Search the Web and Collect Links4
links = quick_web_search(user_query)
print("Web Search Completed!")

# Scrape the Text from the Links
text = scrape_text(links)
answer = summarise(user_query, text)

end_time = time.time()
elapsed_time = "{:.2f}".format(end_time - start_time)

print(f"\nAnswer: {answer}")

print(f"Time Elapsed: {elapsed_time} seconds")