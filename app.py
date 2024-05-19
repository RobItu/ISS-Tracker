# This code calls ISS API to track its current location accurate to the second.
import urllib.request
import json
from dotenv import load_dotenv
import os

load_dotenv()

req = urllib.request.Request("http://api.open-notify.org/iss-now.json")
response = urllib.request.urlopen(req)

obj = json.loads(response.read())

print(f'Data: {obj} ')
print(f"TimeStamp: {obj['timestamp']}")
print(f"Lat/Lon: {obj['iss_position']['latitude']}, {obj['iss_position']['longitude']}")
coordinates= obj['iss_position']['latitude']  + "," + obj['iss_position']['longitude']

# This part of the code will use the location coordinates to get an accurate reading of the territory is currently hovering at

GEOCODING_API_KEY = os.getenv('GEOCODING_API_KEY')

req = urllib.request.Request(f"https://api.opencagedata.com/geocode/v1/json?q={coordinates}&key={GEOCODING_API_KEY}")
response = urllib.request.urlopen(req)

obj = json.loads(response.read())


print(f'Category: {obj["results"][0]["components"]["_category"]}')
print(f'Type: {obj["results"][0]["components"]["_type"]}')

normalized_city = obj["results"][0]["components"].get("_normalized_city", "null")
print(f'_normalized_city: {normalized_city}')

city = obj["results"][0]["components"].get("city", "null")
print(f'city: {city}')

city_district = obj["results"][0]["components"].get("city_district", "null")
print(f'city_district: {city_district}')

continent = obj["results"][0]["components"].get("continent", "null")
print(f'continent: {continent}')

country = obj["results"][0]["components"].get("country", "null")
print(f'country: {country}')

country_code = obj["results"][0]["components"].get("country_code", "null")
print(f'country_code: {country_code}')

county = obj["results"][0]["components"].get("county", "null")
print(f'county: {county}')

house_number = obj["results"][0]["components"].get("house_number", "null")
print(f'house_number: {house_number}')

office = obj["results"][0]["components"].get("office", "null")
print(f'office: {office}')

political_union = obj["results"][0]["components"].get("political_union", "null")
print(f'political_union: {political_union}')

postcode = obj["results"][0]["components"].get("postcode", "null")
print(f'postcode: {postcode}')

road = obj["results"][0]["components"].get("road", "null")
print(f'road: {road}')

state = obj["results"][0]["components"].get("state", "null")
print(f'state: {state}')

state_code = obj["results"][0]["components"].get("state_code", "null")
print(f'state_code: {state_code}')

suburb = obj["results"][0]["components"].get("suburb", "null")
print(f'suburb: {suburb}')

# Maybe we can send a message to it with an API call? We can use Chainlink Functions for that. 

