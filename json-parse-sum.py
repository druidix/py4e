#!/usr/local/bin/python3

import urllib.request
import json

comment_count = 0
json_url = input("Enter JSON URL to parse: ")

print("\nProcessing URL:", json_url)
response = urllib.request.urlopen(json_url)
data = response.read()
print("\nRetrieved", len(data), 'characters')
data.decode()
print("Parsing data...")

for comment_detail in json.loads(data)['comments']:
  comment_count = comment_count + int(comment_detail['count'])

print("\nComment count:", comment_count)