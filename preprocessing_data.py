
import requests
from bs4 import BeautifulSoup
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Adjusted ignore list with more non-text file extensions
ignore_listr = (".pdf", ".jpeg", ".jpg", ".png", ".gif", ".svg", ".mp4", ".mp3", ".zip", ".exe", ".tar", ".gz")

def get_all_links(base_url):
    """Extracts all internal links from the main page, ignoring unwanted file types."""
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = set()
    for a_tag in soup.find_all('a', href=True):
        full_url = urljoin(base_url, a_tag['href'].split("?")[0])  # Normalize URL, ignore query params
        parsed_url = urlparse(full_url)

        if base_url in full_url and not parsed_url.path.lower().endswith(ignore_listr):
            links.add(full_url)

    return links


def scrape_website(url):
    """Scrapes text content from a given URL."""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ')
        return text
    except requests.RequestException:
        return ""

def preprocess_data(web_link,is_deep):
    if not is_deep:
        all_text = scrape_website(web_link)
        clean_text = re.sub(r'\s+', ' ', all_text).strip()
        return clean_text
        
    all_links=get_all_links(web_link)
    all_text=[]
    all_text.append(scrape_website(web_link))
    for link in all_links:
        all_text.append(scrape_website(link))
    print(all_links)
    all_text_content=" ".join(all_text)
    # Clean text by removing extra spaces and newlines
    clean_text = re.sub(r'\s+', ' ', all_text_content).strip()
    # print(clean_text)
    return clean_text
        

if __name__ == "__main__":
    print(preprocess_data("https://www.example.com",False))