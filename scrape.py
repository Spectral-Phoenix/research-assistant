import requests
from bs4 import BeautifulSoup

def scrape_text(links: list[str]):
    """Extracts text from a list of links, appends them, and returns the combined text.

    Args:
        links (list[str]): A list of URLs to scrape text from.

    Returns:
        str: The combined text extracted from all links, or an error message if any.
    """

    scraped_text = ""

    for link in links:
        try:
            response = requests.get(link)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "lxml")
                page_text = soup.get_text(separator=" ", strip=True)[:5000]
                scraped_text += page_text + "\n"  # Append with newline for clarity
            else:
                scraped_text += f"Failed to retrieve '{link}': Status Code {response.status_code}\n"

        except Exception as e:
            scraped_text += f"Failed to retrieve '{link}': {e}\n"

    return scraped_text.strip()  # Remove any leading/trailing whitespace