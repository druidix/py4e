#!/usr/local/bin/python3

def computepay(hrs, rate):
  regular_hours = 40.0
  overtime_multiplier = 1.5
  overtime_pay = 0.0

  if hrs <= regular_hours:
    return hrs * rate
  else:
    overtime_hours = hrs - regular_hours
    overtime_pay = overtime_hours * rate * overtime_multiplier
    return (regular_hours * rate) + overtime_pay

hrs = float(input("Enter hours:"))
rate = float(input("Enter rate:"))

print(computepay(hrs, rate))
