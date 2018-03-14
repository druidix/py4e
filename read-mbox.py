#!/usr/local/bin/python3

fname = input("Enter file name: ")
fh = open(fname)
count = 0
ratings_total = 0
ratings_avg = 0

for line in fh:
  if line.startswith("X-DSPAM-Confidence:"):
    count += 1
    ratings_total += float(line[line.rfind(' '):])
  else:
    continue
fh.close()
print("Average spam confidence:", ratings_total / count)

