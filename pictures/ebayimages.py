import requests
import json

# eBay API endpoint for the Finding API

api_endpoint = 'https://svcs.ebay.com/services/search/FindingService/v1'



# eBay API credentials

app_id = 'your_app_id_here'

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

response.raise_for_status()


# Parse the JSON response

data = json.loads(response.text)


# Extract the picture URLs from the response

search_result = data['findItemsAdvancedResponse'][0]['searchResult'][0]

if 'item' in search_result:
    picture_urls = [item.get('galleryURL', [])[0] for item in search_result['item']]

else:
    picture_urls = []


# Download the pictures
for i, picture_url in enumerate(picture_urls):
    response = requests.get(picture_url)
    response.raise_for_status()
    with open(f'image_{i}.jpg', 'wb') as f:
        f.write(response.content)


print(f'Downloaded {len(picture_urls)} pictures')