import requests
import string
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


inp = input('WHAT ITEM ARE YOU SEARCHING FOR?')

ebay_url = 'https://poshmark.com/search?query=' + inp + '%20&type=listings&src=dir'
response = requests.get(ebay_url)

soup = BeautifulSoup(response.text, "html.parser")

tagsname = soup.findAll(class_="title__condition__container")
tagscost = soup.findAll(class_="p--t--1 fw--bold")
listing_sizes = soup.findAll(class_="tile__details__pipe__size")

yeezy_gaplisting = []
for i in range(1, len(tagsname)):
    title = " ".join(str(tagsname[i].text).split())
    yeezy_gaplisting.append([title])

yeezy_gaplistingsize = []
for i in range(1, len(tagsname)):
    if len(listing_sizes) > i:
        size = " ".join(str(listing_sizes[i].text).split())
    else:
        size = ''
    yeezy_gaplistingsize.append([size])

yeezy_gaplistingcost = []
for i in range(1, len(tagsname)):
    price_text = " ".join(str(tagscost[i].text).split())
    price = float(''.join(filter(str.isdigit, price_text))) 
    yeezy_gaplistingcost.append([price])

print(yeezy_gaplistingsize)

df = pd.DataFrame(np.column_stack([yeezy_gaplisting, yeezy_gaplistingcost, yeezy_gaplistingsize]), columns=['Item', 'Cost', 'size'])
df.to_csv(inp + '-poshmark.xls')

print(df.describe())
