#!/usr/local/bin/python3

hrs = float(input("Enter hours:"))
rate = float(input("Enter rate:"))

regular_hours = 40.0
overtime_multiplier = 1.5
overtime_pay = 0.0
total_pay = 0.0

if hrs <= regular_hours:
  total_pay = hrs * rate
else:
  overtime_hours = hrs - regular_hours
  overtime_pay = overtime_hours * rate * overtime_multiplier
  total_pay = (regular_hours * rate) + overtime_pay

print(total_pay)
