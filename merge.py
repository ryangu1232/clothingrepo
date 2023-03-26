import pandas as pd

# reading csv files
data1 = pd.read_csv('nike-listing-ebay.csv')
data2 = pd.read_csv('yeezy-gap-listing-ebay.csv')

# using merge function by setting how='outer'
output4 = pd.merge(data1, data2,
				on='yeezy_gaplisting',
				how='outer')

# displaying result
print(output4)