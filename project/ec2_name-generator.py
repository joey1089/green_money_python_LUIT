# **EC2 Random Name Generator**
# The Python Script should:
# 1. Allow the user to input how many EC2 instances they want names for and output 
# the same amount of unique names.
# 2. Allow the user to input the name of their department that is used in the unique name.
# 3. Generate random characters and numbers that will be included in the unique name.
# ADVANCED
# The only departments that should use this Name Generator are the Marketing, 
# Accounting, and FinOps Departments. List these departments as options and 
# if a user puts another department, print a message that they should not use this 
# Name Generator. Be sure to account for incorrect upper or lowercase letters in the 
# correct department. Example: a user inputs accounting vs Accounting.
# COMPLEX
# Turn the above into a Function and execute the Function to verify it works.
import random
import os

def clr_scrn():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def generate_names(dept_names,num_of_ec2):
    '''This method prints the auto generates unique names of the given department'''
    # Get the random characters and numbers - to get unique name.
    password_list = []
    for char in range(0,8):
        password_list += random.choice(letters)
    for char in range(0,8):
        password_list += random.choice(numbers)
    str_list_names = []
    count = 0
    while count != num_of_ec2:
        gen_ec2_names = random.sample(password_list,10)
        str_gen_names = [str(i) for i in gen_ec2_names]
        convert_strec2 = dept_names+"_"+"".join(str_gen_names)
        # print("Department EC2 Instance name : ",convert_strec2.replace(" ",""))
        str_list_names.append(convert_strec2.replace(" ",""))
        count += 1
    return str_list_names

def verify_names(generate_ec2_names):
    '''This method verifies all the generated ec2 names are unique'''
    if len(set(generate_ec2_names)) == len(generate_ec2_names):
        return True
    else:
        return False


clr_scrn()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num_of_ec2 = int(input("How many EC2 instances are needed : "))
dept_names = str(input("Choose your department type either - Marketing, Accounting or Fin Ops : ")).title()
generate_ec2_names = generate_names(dept_names,num_of_ec2)  
if verify_names(generate_ec2_names):
    print("All the generated EC2 Instances names are unique ")
else:
    print("Not all are unique ")
if dept_names == 'Marketing':      
    print("\n Marketing Department EC2 Names : ",generate_ec2_names)
   
elif dept_names == 'Accounting':
    print("\n Accounting Department EC2 Names : ",generate_names(dept_names,num_of_ec2))
  
elif dept_names == 'Fin Ops':
    print("\n FinOps Department EC2 Names :",generate_names(dept_names,num_of_ec2))

else:
    print("You can't use Name Genertor for your department !")






