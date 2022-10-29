#!/usr/bin/env python3

message1 = input("Enter a message: ")
print("Length of the message: ",len(message1))
print("First character:", message1[0])
print("Last character:", message1[-1])
print("Middle character:", message1[int(len(message1)/2)])
print("Even index characters:", message1[0::2])
print("Odd index characters:", message1[1::2])
print("Reversed message", message1[::-1])



