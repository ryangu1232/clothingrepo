import requests
import json

#creates api endpoint when calls are fufilled
api_endpoint = 'https://svcs.ebay.com/services/search/FindingService/v1'

# eBay API credentials
app_id = 'Ebay API Key (currently pending approval)'


# Set up the request headers
headers = {
     'X-EBAY-SOA-OPERATION-NAME': 'findItemsAdvanced',
     'X-EBAY-SOA-SERVICE-NAME': 'FindingService',
     'X-EBAY-SOA-SERVICE-VERSION': '1.0.0',
     'X-EBAY-SOA-REQUEST-DATA-FORMAT': 'JSON',
     'X-EBAY-SOA-GLOBAL-ID': 'EBAY-US',
     'X-EBAY-SOA-SECURITY-APPNAME': app_id
}

# Set up the request body
payload = {
    'keywords': 'iphone', # replace with your search keywords
    'paginationInput': {
        'entriesPerPage': 10, # replace with your desired number of results
        'pageNumber': 1
     },
    'outputSelector': ['PictureURLLarge'] # retrieve only large pictures
}

# Make the API request
response = requests.post(api_endpoint, headers=headers, json=payload)

# Parse the JSON response
data = json.loads(response.text)

# Extract the picture URLs from the response
picture_urls = []
for item in data['findItemsAdvancedResponse'][0]['searchResult'][0]['item']:
    if 'galleryURL' in item:
        picture_urls.append(item['galleryURL'][0])


# Download the pictures
for i, picture_url in enumerate(picture_urls):
    response = requests.get(picture_url)
    with open(f'image_{i}.jpg', 'wb') as f:
        f.write(response.content)


