import requests
import json

#creates api endpoint when calls are fufilled
endpoint = 'https://svcs.ebay.com/services/search/FindingService/v1'

#Ebay API key
app_id = 'Ebay API Key (currently pending approval)'


#Headers for the request
headers = {
     'X-EBAY-SOA-OPERATION-NAME': 'findItemsAdvanced',
     'X-EBAY-SOA-SERVICE-NAME': 'FindingService',
     'X-EBAY-SOA-SERVICE-VERSION': '1.0.0',
     'X-EBAY-SOA-REQUEST-DATA-FORMAT': 'JSON',
     'X-EBAY-SOA-GLOBAL-ID': 'EBAY-US',
     'X-EBAY-SOA-SECURITY-APPNAME': app_id
}

#Setse up request
payload = {
    'keywords': 'iphone', #replace with search terms
    'paginationInput': {
        'entriesPerPage': 10, #replace with number of search results
        'pageNumber': 1
     },
    'outputSelector': ['PictureURLLarge'] # retrieve only large pictures
}

# Make the API request
response = requests.post(endpoint, headers=headers, json=payload)

# Parse the JSON response
data = json.loads(response.text)

#extracts picture url's
picture_urls = []
for item in data['findItemsAdvancedResponse'][0]['searchResult'][0]['item']:
    if 'galleryURL' in item:
        picture_urls.append(item['galleryURL'][0])


#downloads pictures
for i, picture_url in enumerate(picture_urls):
    response = requests.get(picture_url)
    with open(f'image_{i}.jpg', 'wb') as f:
        f.write(response.content)


