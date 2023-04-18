import requests
import re
from bs4 import BeautifulSoup
ebay_url = 'https://www.ebay.com/sch/yeezy-gap-hoodie'
response = requests.get(ebay_url)

soup = BeautifulSoup(response.text, "html.parser")

tagscost = soup.findAll(class_="s-item__price")
tagsname = soup.findAll(class_="s-item__title")
secondhand = soup.findAll(class_="SECONDARY_INFO")

yeezy_gaplisting = []
for i in range(1, len(tagsname)):
    yeezy_gaplisting.append(tagsname[i].text)

yeezy_gaplistingcost = []
for i in range(1, len(tagsname)):
    yeezy_gaplistingcost.append(str(tagscost[i]))
#print(yeezy_gaplistingcost)

import re

prices = []

for price in yeezy_gaplistingcost:
    price_value = re.findall('\d+\.\d+', price) # find all numbers with decimal points
    if price_value:
        prices.append(float(price_value[0])) # convert string to float and append to prices list

print(prices)


yeezy_gaplistinguse = []
for i in range(1,(len(tagsname))):
    yeezy_gaplistinguse.append( secondhand[i].text)
#print(yeezy_gaplistinguse)



#df = pd.DataFrame(yeezy_gaplisting, columns=['yeezy_gaplisting'])
#df.to_csv('yeezy-gap-listing-ebay.csv')


df = pd.DataFrame(np.column_stack([yeezy_gaplisting, prices, yeezy_gaplistinguse]), columns=['Item', 'Cost', 'Wear'])
df["Cost"] = pd.to_numeric(df["Cost"], errors="coerce")
df.to_csv('yezy-ebay.xls')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df.head())

#base analytics

print(df.describe())
wear_counts = df['Wear'].value_counts()
print(wear_counts)



# create a boxplot
fig, ax = plt.subplots()
plt.boxplot([df[df['Wear'] == 'Brand New']['Cost'], 
             df[df['Wear'] == 'New']['Cost'], 
             df[df['Wear'] == 'Pre-owned']['Cost']],
            labels=['Brand New', 'New', 'Pre-owned'])

# set the title and axis labels
plt.title('Cost Distribution by Wear')
plt.xlabel('Wear')
plt.ylabel('Cost')

# save the plot to a file
fig.savefig('wear_cost_boxplot.png')

# calculate the correlation coefficient between 'Cost' and 'Wear'
corr_coef = df['Cost'].corr(df['Wear'], method='spearman')
print(f"Correlation coefficient between 'Cost' and 'Wear': {corr_coef:.2f}")
