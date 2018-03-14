#!/usr/local/bin/python3

fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
  print(line.rstrip().upper())
fh.close()
