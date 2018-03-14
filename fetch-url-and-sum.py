#!/usr/local/bin/python3

import urllib.request
from bs4 import BeautifulSoup

file_url = 'http://py4e-data.dr-chuck.net/comments_71713.html'
sum = 0

response = urllib.request.urlopen(file_url)
soup = BeautifulSoup(response, 'html.parser')
spans = soup('span')

for span in spans:
  sum = sum + int(span.contents[0])

print(sum)