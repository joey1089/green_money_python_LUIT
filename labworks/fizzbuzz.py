#!/usr/bin/python3.10

# Implementing python code for Fizz Buzz logic
value = int(input("Enter an integer value: "))

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)

# ACG logic
upper_number = int(input("How many values should we process: "))

for number in range(1, upper_number + 1):
  if number % 3 == 0 and number % 5 == 0:
      print("FizzBuzz")
  elif number % 3 == 0:
      print("Fizz")
  elif number % 5 == 0:
      print("Buzz")
  else:
      print(number)
