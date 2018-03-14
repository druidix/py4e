#!/usr/local/bin/python3

count = 0
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
  line.rstrip()
  words_in_line = []
  for word in line.split():
    words_in_line.append(word)
  # print(words_in_line)
  if len(words_in_line) > 0 and words_in_line[0] == 'From':
    count = count + 1
    print(words_in_line[1])
  else:
    continue
fh.close()

print("There were", count, "lines in the file with From as the first word")