import csv
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import requests


# launch a web browser and navigate to the search results page
driver = webdriver.Chrome('/path/to/chromedriver')
driver.get('https://poshmark.com/search?query=nike&type=listings&src=dir')


# wait for the page to load and retrieve the HTML content
html = driver.page_source


# parse the HTML content with BeautifulSoup and locate the <img> tags
soup = BeautifulSoup(html, 'html.parser')
img_tags = soup.find_all('img')


# create a list to hold the image data
image_data = []



# download each image from its URL and save it to your local filesystem
for img_tag in img_tags:
    img_url = img_tag.get('src')
    response = requests.get(img_url)
    file_name = f"{img_tag['alt']}.jpg"
    with open(file_name, 'wb') as f:
        f.write(response.content)
    image_data.append([img_url, file_name])


# closes the web browser
driver.quit()


# save the image data to a CSV file
with open('image_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Image URL', 'File Name'])
    for row in image_data:
        writer.writerow(row)