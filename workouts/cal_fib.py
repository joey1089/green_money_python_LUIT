#!/usr/bin/python3.10
# Calculate fibonacci
# Sequence starts with 0 and then its 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ...
# Formula to calculate fib Fn = Fn-1 + Fn-2

def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-1) + fib(num-2)

fib_num = int(input("Enter a number to calculate Fibonacci : "))
print(f"Your Finonacci number :{fib(fib_num)}")
