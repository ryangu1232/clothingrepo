# second retro 2/13 for a more expansive view on api and how to use them with pandas 

import requests 
import json 

responses = requests.get('https://api.covid19api.com/summary').text

##print(responses)

responseinfo = json.loads(responses)
# makes responses a python dictionary 
print(responseinfo)

#in this dictonary countries is a key value which is connected to a whole bunch of values. 

#create a open dictionary country list
country_list = []
#goes through the list of countries in the data, adds the country and its corresponding deaths in the dictionary.
for country_info in responseinfo['Countries']:
 country_list.append([country_info['Country'], country_info['TotalDeaths']])

print(country_list)

import pandas as pd

country_df = pd.DataFrame(data=country_list, columns=['Country', 'Total_Confirmed'])
print(country_df.head(10))