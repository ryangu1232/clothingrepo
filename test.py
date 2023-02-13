import requests

url = "https://google.com"

'''response = requests.get(url)
print(response)
'''
#print 200 meaning request was succsesful

url = "http://api.weatherapi.com/v1/current.json?key=9797749cd6764933844220709230602&q=London&aqi=no"

#signed up for weatherapi account and using this url to practice before starting on real project. 
#created a google doc to learn w me. 
response = requests.get(url)
json = response.json()
##cant use .location
print(response)
print(json["location"])
#output is the location of this weather information is the city of london specifically lat:51.52 lon:-0.11 at the current time
temperature = json["current"]["temp_f"]
print(temperature)
#gives me exactly current temperature right now in london pretty cool
#ryan g's job:create a plot of this using the past weeks temp in london and graph it out

