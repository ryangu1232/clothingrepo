import requests
import pandas as pd

data2 = pd.read_csv('merge.csv')

row_number = int(input('Enter the row number: '))

# Check if there is a row here
if row_number >= 0 and row_number < len(data2):
    
    row_data = data2.iloc[row_number]

    # Get the image link from the row data
    image_link = row_data['ImgLink']

    # Output the image link
    print(image_link)
else:
    print('Invalid row number. Please try again.')



image = image_link

    #still working on how to ask for input of a link

     #we will learn how to pull an image link and display it somewhere next


picture = requests.get(image)

print(picture.content)

with open('imagefordemo:\notredame.png','wb') as f:
    f.write(picture.content)
