import pandas as pd

# reading csv files
data1 = pd.read_csv('nike-listing-ebay.csv')
data2 = pd.read_csv('yezy-ebay.xls')


# using merge function by setting how='outer'
output4 = pd.merge(data1, data2, #data3,
				on='yeezy_gaplisting',
				#right_on = 'grailed_listing',
				how='outer')

# displaying result

output4.to_csv('merge.csv')