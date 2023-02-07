import requests
#bs4 pulls data from the Beautiful Soup Libraries which helps me pull things from HTML files
from bs4 import BeautifulSoup 

#city that is used 

city  = input('''
What city would you like to research?
''')
 
# create url to be used in searches
url = "https://www.google.com/search?q="+"weather"+city


html = requests.get(url).content
 
# getting the data and putting it in soup
soup = BeautifulSoup(html, 'html.parser')

print(soup)