import requests
from bs4 import BeautifulSoup


def scrape_text(links):
    content_list = []
    for link in links:
        session = requests.Session()
        response = session.get(link, timeout=4)
        soup = BeautifulSoup(response.content, 'lxml', from_encoding=response.encoding)
        for script_or_style in soup(["script", "style"]):
            script_or_style.extract()
        raw_content = get_content_from_url(soup)
        lines = (line.strip() for line in raw_content.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        content = "\n".join(chunk for chunk in chunks if chunk)
        content_list.append(content)
    return content_list


def get_content_from_url(soup):
    """Get the text from the soup
    Args:
        soup (BeautifulSoup): The soup to get the text from
    Returns:
        str: The text from the soup
    """
    text = ""
    tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5']
    for element in soup.find_all(tags):  # Find all the <p> elements
        text += element.text + "\n"
    return text

  # Replace with your list of links

def scrape(links):
    content_list = scrape_text(links)
    for content in content_list:
        return content
