import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#input = input("Enter search term: ")
#underneath is a different way of how to work with strings by adding the code in the string itself which i am going to start using because of easy.
#grailed_url = f'https://www.grailed.com/search?query={input.replace(" ", "%20")}'
grailed_url = 'https://www.depop.com/search/?q=yeezy+gap'
response = requests.get(grailed_url)
print(response)


soup = BeautifulSoup(response.text, "html.parser")

tagscost = soup.findAll(class_="sc-jqUVSM Pricestyles__FullPrice-sc-__sc-1iqvn14-0 cZBwWq cZNcvW")
tag = soup.find('a', {'class': 'styles__ProductCard-sc-__sc-13q41bc-3 fBWGBN'})
href = tag['href']
print(href)
print(len(href))
print(len(tagscost))

tags = soup.find_all('a', class_='styles__ProductCard-sc-__sc-13q41bc-3 fBWGBN')


yeezy_gaplisting = []
for i in range(0, len(tagscost)):
    yeezy_gaplisting.append(href[i])

yeezy_gaplistingcost = []
for i in range(0, len(tagscost)):
    yeezy_gaplistingcost.append(str(tagscost[i].text))
#print(yeezy_gaplistingcost)

prices = []

for price in yeezy_gaplistingcost:
    price_value = re.findall('\d+\.\d+', price) # find all numbers with decimal points
    if price_value:
        prices.append(float(price_value[0])) # convert string to float and append to prices list

print(prices)


df = pd.DataFrame(np.column_stack([yeezy_gaplisting, prices]), columns=['Item', 'Cost'])
df["Cost"] = pd.to_numeric(df["Cost"], errors="coerce")
df.to_csv('yezy-grailed.xls')
print(df)
