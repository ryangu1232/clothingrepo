import requests
import string
from bs4 import BeautifulSoup

inp = input('WHAT ITEM ARE YOU SERACHING FOR?')

ebay_url = 'https://poshmark.com/search?query=' + inp + '%20&type=listings&src=dir'
response = requests.get(ebay_url)

#print(response) working = 200
soup = BeautifulSoup(response.text, "html.parser")
##print(soup) succsesful in bringing html code from ebay website

tagsname = soup.findAll(class_ = "title__condition__container")
tagscost = soup.findAll(class_ = "p--t--1 fw--bold")


yeezy_gaplisting = []
for i in range(1,(len(tagsname))):
   # (DOESNT WORK) yeezy_gaplisting.append(str(tagsname[i].text).translate({ord(c): None for c in string.whitespace}))
    #origional code  yeezy_gaplisting.append(tagsname[i].text +" : "+ tagscost[i].text + " wear:  ")
    yeezy_gaplisting.append(" ".join(str(tagsname[i].text).split())+ " ".join(str(tagscost[i].text).split()))
# poshmarks title is very hard to seperate from other information they give, without this additional code 
# there would be multiple lines and spaces which would make it harder to combine it with other lists in websites. 
# replace the code with the matching line in ebay.py to see the difference in output. 
# DOESNT WORK yeezy_gaplisting = [x.strip('\n            ') for x in yeezy_gaplisting]

print(yeezy_gaplisting)

import pandas as pd
df = pd.DataFrame(yeezy_gaplisting, columns=['yeezy_gaplisting'])
df.to_csv(inp+'-listing-ebay.csv')
