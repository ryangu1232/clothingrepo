import requests
from bs4 import BeautifulSoup
ebay_url = 'https://www.ebay.com/sch/yeezy-gap-hoodie'
response = requests.get(ebay_url)

#print(response) working = 200
soup = BeautifulSoup(response.text, "html.parser")
##print(soup) succsesful in bringing html code from ebay website

tagscost = soup.findAll(class_ = "s-item__price")
tagsname = soup.findAll(class_ = "s-item__title")
secondhand = soup.findAll(class_ = "SECONDARY_INFO")

yeezy_gaplisting = []
for i in range(1,(len(tagsname))):
    yeezy_gaplisting.append(tagsname[i].text +" : "+ tagscost[i].text + " wear:  "+ secondhand[i].text)
print(yeezy_gaplisting)

import pandas as pd
df = pd.DataFrame(yeezy_gaplisting, columns=['yeezy_gaplisting'])
df.to_csv('yeezy-gap-listing-ebay.csv')