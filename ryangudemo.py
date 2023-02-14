import requests
#bs4 pulls data from the Beautiful Soup Libraries which helps me pull things from HTML files
from bs4 import BeautifulSoup 

loopnumber = int(input('''How many times do you want to run this code'''))

#city that is used 

for i in range(0,loopnumber):
    city  = input('''
    What city would you like to research?
    ''')
 
# create url to be used in searches
    url = "https://www.google.com/search?q="+"weather"+city

#uses requests package to get content from website
    html = requests.get(url).content
 
# getting the data and putting it in soup
    soup = BeautifulSoup(html, 'html.parser') 
    #html.parser

    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    print(temp)
    print(str)

print(soup.title)


