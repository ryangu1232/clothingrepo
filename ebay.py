import requests
from bs4 import BeautifulSoup
ebay_url = 'https://www.ebay.com/sch/yeezy-gap'
response = requests.get(ebay_url)

#print(response) working = 200
soup = BeautifulSoup(response.text, "html.parser")
##print(soup) succsesful in bringing html code from ebay website

tags = soup.findAll(class_ = "s-item__title")
#print(tags[1].text) working gives title of 1 

yeezy_gaplisting = []
for i in range(1,len(tags)):
    yeezy_gaplisting.append(tags[i].text)
print(yeezy_gaplisting)

import pandas as pd
df = pd.DataFrame(yeezy_gaplisting, columns=['yeezy_gaplisting'])
df.to_csv('yeezy-gap-listing-ebay.csv')