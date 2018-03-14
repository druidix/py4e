#!/usr/local/bin/python3

import re

fname = input("Enter file name: ")
fh = open(fname)
sum = 0

for line in fh:
  nums_in_line = re.findall('[0-9]+', line)
  if len(nums_in_line) > 0:
    for num_string in nums_in_line:
      sum = sum + int(num_string)
  else:
    continue
fh.close()
print(sum)
