<<<<<<< HEAD
clothingrepo

clothing test test test 
=======
# clothingrepo
ABOUT: 
A website that combines clothing, accessories, and other items sold on second-hand merchant sites together. 

PROGRESS:
Currently, code is about halfway done and is able to pull individual search results given the search link. For example, upon putting in the link in ebay.py, the code will display the top search results on ebay. In the future, we will work to integrate ebay.py, grailed.py, together. 
UPDATE 4/17: We are 75% done we are able to integrate 2 webscrapers together, and added some statistical analysis. 

GET STARTED: 
To run this program, you will need to have Python installed on your computer. You will also need to install the following Python libraries:

requests
beautifulsoup4
pandas
numpy
matplotlib
selenium 

To install these libraries, you can use pip, the Python package manager

INDIVIDUAL FILE USES:
- merge.py
    - takes csv files produced by ebay.py and poshmark.py and combines them together. Still unsure on how to create filters/sort prices, etc. 
- ebay.py  
    - The program will scrape eBay listings for Yeezy Gap Hoodies and create a dataset called yeezy-ebay.xls. It will also generate a boxplot called wear_cost_boxplot.png showing the distribution of prices by wear condition.
    - Gives further analytics such as dataset summary, count number of listings, and finds the correlation coefficient between Wear and Cost. 

- poshmark.py
    - same thing as ebay.py but without the statstics or updates since 4/3 and with poshmark listings isntead of ebay ones. 
    - as of 5/2 poshmark.py now is organized the same way as ebay which has a numerical value for price and also pulls the size. 
        - unlike ebay.py poshmarks website does not have wear listed so a lot of the statsitcs can 

-pictures file
    - Ryan gu is working on turning pictures from urls into seeable images. Code does not work due to api key which is being requested right now. 
    -updated now working but needs to install selenium 

Updates: 2/13/2023
Choudhury's code so far can pull covid cases from the internet as well as deaths. Gu's code asks for user input and pulls weather data. Have not worked with clothing yet as we are still learning how to use website API 
*testing a commit from vs code for the readme
>>>>>>> 394549b0a538242183bda9ff507ea763ea86a29c

Updates 3/27/2023
merge.py takes the csv files that grailed.py and ebay.py make and merges them together so that users can see the options that are available for each. 

Updates 4.17

Pictures file is being created so the final listing will have both the name, cost, wear, and the image. 
ebay.py recieved significant changes with the "Cost" list. Now all values are integers. 
ebay.py also has a lot of stastical analysis which in the future can allow users to compare ebay with other platforms. (box plot was also created)
Readme was updated. 
Other files remain unchanged. 

Updates 4/25/2023
ebayimages: 
    - includes try-except blocks to catch and handle different types of errors that can occur during the API request
    - response parsing
    - image downloads 
    - continues downloading pictures even if one or more requests fail.    
    
Update 5/16/2023
    - WORKINGpictures.py code finally works
    - takes images from ebay search query and prints the link. 
    - code takes link of images and prints them when it is called on. 
