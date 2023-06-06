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

   

    try:

        picture = requests.get(image_link)

       

        if picture.status_code == 200:

            with open('imagefordemo:', 'wb') as f:

                f.write(picture.content)

        else:

            print('No image available for this value')

    except requests.exceptions.MissingSchema:

        print('Invalid URL or no image available')

else:

    print('Invalid row number. Please try again.')