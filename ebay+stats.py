import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import string
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import csv

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row[0])  # Assuming each row contains a single word
    return data

# Specify the CSV file to read
csv_filename = 'words.csv'

# Read the data from the CSV file and store it in a variable
words = read_csv_file(csv_filename)

# Convert the list of words into a string without quotes and brackets
words_string = ', '.join(words)

# Print the resulting string

ebay_url = 'https://www.ebay.com/sch/' + words_string 
response = requests.get(ebay_url)


#getting input/ bs html link

soup = BeautifulSoup(response.text, "html.parser")

tagscost = soup.findAll(class_="s-item__price")
tagsname = soup.findAll(class_="s-item__title")
secondhand = soup.findAll(class_="SECONDARY_INFO")
tagscat = soup.findAll(class_="s-item__subtitle")
tagsimage = soup.findAll(class_ = "s-item__image-wrapper image-treatment")
#creating tags 

yeezy_gaplisting = []
for i in range(1, len(tagsname)):
    yeezy_gaplisting.append(tagsname[i].text)

yeezy_gaplistingimg = []
for tag in tagsimage[1:]:
    img_url = tag.find('img')['src']
    yeezy_gaplistingimg.append(img_url)
    #print(img_url)

yeezy_gaplistingcost = []
for i in range(1, len(tagsname)):
    yeezy_gaplistingcost.append(str(tagscost[i]))

prices = []

for price in yeezy_gaplistingcost:
    price_value = re.findall('\d+\.\d+', price) # find all numbers with decimal points
    if price_value:
        prices.append(float(price_value[0])) # convert string to float and append to prices list

yeezy_gaplistinguse = []
for i in range(1,(len(tagsname))):
    yeezy_gaplistinguse.append( secondhand[i].text)
#print(yeezy_gaplistinguse)

yeezy_gaplistingcategory = []
for i in range(1, len(tagsname)):
    if len(tagscat) > i:
        yeezy_gaplistingcategory.append(tagscat[i].text)
    else:
        yeezy_gaplistingcategory.append("N/A")

#creating lists



df = pd.DataFrame(np.column_stack([yeezy_gaplisting, prices, yeezy_gaplistinguse, yeezy_gaplistingcategory, yeezy_gaplistingimg]), columns=['Item', 'Cost', 'Wear', 'Category', "ImgLink"])
df["Cost"] = pd.to_numeric(df["Cost"], errors="coerce")

csv_filename = f'{words_string.lower()}-ebay.xls'
df.to_csv(csv_filename)


#combine lists to create df


print(df.describe())
wear_counts = df['Wear'].value_counts()

#base analytics


fig, ax = plt.subplots()
plt.boxplot([df[df['Wear'] == 'Brand New']['Cost'], 
             df[df['Wear'] == 'New']['Cost'], 
             df[df['Wear'] == 'Pre-owned']['Cost']],
            labels=['Brand New', 'New', 'Pre-owned'])

plt.title('Cost Distribution by Wear')
plt.xlabel('Wear')
plt.ylabel('Cost')


fig.savefig('wear_cost_boxplot.png')


categories = {}
for i in range(len(yeezy_gaplisting)):
    category = yeezy_gaplistingcategory[i]
    price = prices[i]
    if category not in categories:
        categories[category] = []
    categories[category].append(price)
#dictionary for the histogram
    
fig, ax = plt.subplots(figsize=(10, 5))
plt.hist(df['Cost'], bins=50)

for category, prices in categories.items():
    plt.hist(prices, bins=10, alpha=0.5, label=category)

plt.legend(loc='upper right')
plt.xlabel('Price')
plt.ylabel('Count')
plt.title('Price Distribution by Category')
plt.show()
fig.savefig('category_price_histo.png')

#box plot + histogram 

corr_coef = df['Cost'].corr(df['Wear'], method='spearman')
print(f"Correlation coefficient between 'Cost' and 'Wear': {corr_coef:.2f}")
#correlaiton coefficient

total_listings = len(df)
preowned_listings = len(df[df['Wear'] == 'Pre-Owned'])
preowned_percentage = preowned_listings / total_listings * 100
print(f"Percentage of pre-owned listings:" + str(preowned_percentage))

# Find the total number of listings, the number of listings with wear labeled as "Pre-owned", and the percentage of listings with wear labeled as "Pre-owned"
