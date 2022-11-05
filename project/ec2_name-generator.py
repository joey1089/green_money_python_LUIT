# **EC2 Random Name Generator**
import random
import os

def clr_scrn():
    '''This method clears the screen'''
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def generate_names(dept_name,no_of_ec2):
    '''This method prints the auto generates unique names of the given department'''
    str_list_names = []
    getpwdgen = pwdgen()
    count = 0
    while count != no_of_ec2:
        gen_ec2_names = random.sample(getpwdgen,10)
        str_gen_names = [str(i) for i in gen_ec2_names]
        convert_strec2 = dept_name+"_"+"".join(str_gen_names)
        str_list_names.append(convert_strec2.replace(" ",""))
        count += 1
    if (verify_names(str_list_names)):
        return str_list_names
    return "Generated Names are not unique - its a Error in code !"

def verify_names(list_names):
    '''This method verifies all the generated ec2 names are unique'''    
    if len(set(list_names)) == len(list_names):
        print("All the generated EC2 Instances names are unique !")
        return True
    else:
        return "Not all generated EC2 Instances names are unique !!!"

def pwdgen():
    '''This method returns password combined with letters and numbers.'''
    password_list = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in range(0,8):
        password_list += random.choice(letters)
    for char in range(0,8):
        password_list += random.choice(numbers)
    return password_list

clr_scrn()
print("========================== EC2 Instances Name Generator =======================================")
num_of_ec2 = int(input("How many EC2 instances are needed : "))
dept_names = str(input("Choose your department, type either - 'Marketing', 'Accounting' or 'Fin Ops' : ")).title()

if dept_names == 'Marketing':      
    print("Marketing Department EC2 Names : ",generate_names(dept_names,num_of_ec2) )
elif dept_names == 'Accounting':
    print("Accounting Department EC2 Names : ",generate_names(dept_names,num_of_ec2) )
elif dept_names == 'Fin Ops':
    print("FinOps Department EC2 Names : ",generate_names(dept_names,num_of_ec2) )
else:
    print("You can't use Name Genertor for your department !")






