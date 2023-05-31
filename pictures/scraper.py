import requests
from bs4 import BeautifulSoup

def scrape_image_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    img_tag = soup.find("img")
    image_url = img_tag["src"]
    return image_url

# Example usage:
url = "https://example.com"  # Replace with the webpage URL
image_url = scrape_image_url(url)
print(image_url)
