#!/usr/bin/env python3

myList = [7,5,8,4,3,0,6,1]
myList.sort()
print(myList)
print(myList[::-1]) # Reverse the list without reversed keyword
print(myList.index(3))
print(4 not in myList)
myList.insert(0,-1)
myList.insert(3,2)
print("New MyList :",myList)
#myList.sort()
#myList.insert(9,15)
print(sorted(myList)) # Sorted list
print(list(reversed(myList)) )# Reverse the list
# can also do it in one step both sort and reverse but all items should be of same type
print(list(reversed(sorted(myList)))) # will get the same results

