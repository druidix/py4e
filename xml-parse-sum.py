#!/usr/local/bin/python3

import urllib.request
import xml.etree.ElementTree as ET

comment_count = 0
xml_url = input("Enter XML URL to parse: ")

print("\nProcessing URL:", xml_url)
response = urllib.request.urlopen(xml_url)
data = response.read()
print("\nRetrieved", len(data), 'characters')
data.decode()
print("Parsing data...")

tree = ET.fromstring(data)
comments = tree.findall('comments')

for comment_obj in comments:
  comment_details = comment_obj.findall('comment')
  for comment_detail in comment_details:
    comment_count = comment_count + int(comment_detail.find('count').text)

print("Sum of comment counts:", comment_count)