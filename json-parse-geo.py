#!/usr/local/bin/python3

import urllib.request
import json

json_url = None
api_base_url = 'http://py4e-data.dr-chuck.net/geojson?'
address = input("Enter address to look up: ")

json_url = api_base_url + urllib.parse.urlencode({'address': address})
print("\nProcessing URL:", json_url)
response = urllib.request.urlopen(json_url)
data = response.read()
print("\nRetrieved", len(data), 'characters')
data.decode()
print("Parsing data...")

print("Place id", json.loads(data)['results'][0]['place_id'])