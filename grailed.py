import requests
from bs4 import BeautifulSoup
grailed_url = 'https://www.ebay.com/sch/yeezy-gap-hoodie'
response = requests.get(grailed_url)

#print(response) working = 200
soup = BeautifulSoup(response.text, "html.parser")
##print(soup) succsesful in bringing html code from ebay website

tagscost = soup.findAll(class_ = "s-item__price")
tagsname = soup.findAll(class_ = "s-item__title")
secondhand = soup.findAll(class_ = "SECONDARY_INFO")

grailedlisting = []
for i in range(1,(len(tagsname))):
    grailedlisting.append(tagsname[i].text +" : "+ tagscost[i].text + " wear:  "+ secondhand[i].text)
print(grailedlisting)

import pandas as pd
df = pd.DataFrame(grailedlisting, columns=['grailed_listing'])
df.to_csv('grailed.csv')