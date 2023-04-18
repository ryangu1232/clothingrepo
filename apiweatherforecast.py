import requests

url = "https://api.tomorrow.io/v4/timelines"

querystring = {
"location":"47, -122",
"fields":["temperature", "cloudCover"],
"units":"imperial",
"timesteps":"1d",
"apikey":"AGhVJATDTWXkoNv0CUrE1pR5MFLLSyWy"}

response = requests.request("GET", url, params=querystring)
print(response.text)

t = response.json()['data']['timelines'][0]['intervals'][0]['values']['temperature']

print("Weather Forecast")
print("================")

results = response.json()['data']['timelines'][0]['intervals']
for daily_result in results:
    date = daily_result['startTime'][0:10]
    temp = round(daily_result['values']['temperature'])
    print("On",date,"it will be", temp, "F")

print(daily_result)