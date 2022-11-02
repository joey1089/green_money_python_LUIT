#!/bin/python3

#======================================== weird numbers =======================================
#This part of the code is for hackrank problem
def weirdnumbers(num):
    '''Find a given number is weird or not'''
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n in range(2,5):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6,20):
        print("Weird")
    elif n % 2 == 0 and n >= 20:
        print("Not Weird")


#========================================= while loop testing =================================
#This part of the code is for hackrank problem
def square_root(num):
    '''This function prints out the square root upto the given number.'''
    i = 0
    while i <= num:
        print(i*i)
        i += 1

#====================== Counting Odd Numbers ==================================================
def count_oddnum(num):
    '''This fn prints out the odd numbers upto the given number.'''
    count = 0
    while count <= num:
        if count % 2 == 0:
            count += 1            
        print(f"Odd Numbers : {count}")
        count += 1


if __name__ == '__main__':
    n = int(input("Enter a number : ").strip())
    strchoice = input("\n type (1)for weird number, (2)for square roots and (3) for Odd Numbers :")
    if strchoice == '1':
        weirdnumbers(n)
    elif strchoice == '2':
        square_root(n)
    elif strchoice == '3':
        count_oddnum(n)
    else:
        print("\n Wrong choice try again !")
        
