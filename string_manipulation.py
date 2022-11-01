#!/usr/bin/python3.10
# str_cons = 'test_this_out'
# print(str_cons.capitalize())
# print(id(str_cons))
# print(id('test_this_out'))
# print(str_cons)
# print(str_cons[-1])
# print(str_cons[-2])
# print(str_cons[-3])
# print(str_cons[4])
# print(str_cons[0:2])
#  >>> test_str = 'testing'
# >>> test_str[2:]
# 'sting'
# >>> test_str[2:len(test_str)]
# 'sting'
# >>> test_str[0:3]
# 'tes'
# >>> test_str[1:3]
# 'es'
# >>> test_str[3:5]
# 'ti'
# >>> test_str[0:8]
# 'testing'
# >>> test_str[::-1]
# 'gnitset'
# >>> test_str[0::8:2]
#   File "<stdin>", line 1
#     test_str[0::8:2]
#                  ^
# SyntaxError: invalid syntax
# >>> test_str[0:8:2]
# 'tsig' 
#=================================================================

message = input("Enter a message: ")

print("Lowercase:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

words = message.split()
print("Words:", words)
# strwords = " "
# strwords = ",".join(words) # converting to string doesn't work instead convert it to tuple
# print("String of Words : ", strwords.lower()) 
sorted_words = list(sorted(words))
print(sorted_words)

print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1],"\n")

