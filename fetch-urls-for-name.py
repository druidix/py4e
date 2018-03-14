#!/usr/local/bin/python3

import re
import urllib.request
from bs4 import BeautifulSoup

# start_url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
start_url = 'http://py4e-data.dr-chuck.net/known_by_Joel.html'
position = None
repeat_count = None
count = 0

def fetch_url_contents(url):
  response = urllib.request.urlopen(url)
  return BeautifulSoup(response, 'html.parser')

print("\n\nStarting with URL:", start_url)

# The list of anchors below is a zero-based array, adjust for that
position = int(input("\nEnter position: ")) - 1
repeat_count = int(input("Enter repeat count: "))

soup = fetch_url_contents(start_url)
anchors = soup('a')

for num in range(0, repeat_count):
  print("Processing URL:", anchors[position].get('href', None))
  soup = fetch_url_contents(anchors[position].get('href', None))
  anchors = soup('a')

# When the above loop exits, soup should be set to the response object of the page we need
# Capture the h1 tag and regex the name out of it
h1_tag = soup('h1')[0]
name_string = str(h1_tag.contents[0])

p = re.compile(r'that\s\S+\sknows')
m = p.search(name_string)
print(m.group().split()[1])