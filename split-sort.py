#!/usr/local/bin/python3

words_in_file = []

fname = input("Enter file name: ")

fh = open(fname)

for line in fh:
  line.rstrip()
  for word in line.split():
    if word in words_in_file:
      continue
    else:
      words_in_file.append(word)
fh.close()
words_in_file.sort()
print(words_in_file)