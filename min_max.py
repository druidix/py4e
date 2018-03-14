#!/usr/local/bin/python3

largest = None
smallest = None
while True:
    num = input()
    if num == "done" : break
    try:
      num = int(num)
      if (largest is None and smallest is None):
        largest = num
        smallest = num
      if (num > largest):
        largest = num
      if (num < smallest):
        smallest = num
    except:
      print("Invalid input")
      continue

print("Maximum is", largest)
print("Minimum is", smallest)
