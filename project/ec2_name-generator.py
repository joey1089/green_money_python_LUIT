# **EC2 Random Name Generator**
import random
import string
import os

def clr_scrn():
    '''This method clears the screen'''
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def get_menu(no_ec2):
    dept_names = str(input("Choose your department, type either - 'Marketing', 'Accounting' or 'Fin Ops' : ")).title()

    if dept_names == 'Marketing':      
        print("\nMarketing Department EC2 Names : ",generate_names(dept_names,no_ec2) )
    elif dept_names == 'Accounting':
        print("\nAccounting Department EC2 Names : ",generate_names(dept_names,no_ec2) )
    elif dept_names == 'Fin Ops':
        print("\nFinOps Department EC2 Names : ",generate_names(dept_names,no_ec2) )
    else:
        print("You can't use Name Genertor for your department !")


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
        print("\nAll the generated EC2 Instances names are unique !")
        return True
    else:
        return "Not all generated EC2 Instances names are unique !!!"

def pwdgen():
    '''This method returns password combined with letters and numbers.'''
    password_list = []
    letters = string.ascii_letters    
    numbers = string.digits
    for char in range(0,8):
        password_list += random.choice(letters)
    for char in range(0,8):
        password_list += random.choice(numbers)
    return password_list

clr_scrn()
print("\n========================== EC2 Instances Name Generator =======================================\n")
count = 3
while count != 0 :
    num_of_ec2 = int(input("How many EC2 instances are needed : "))
    if num_of_ec2 >= 1:
        get_menu(num_of_ec2)
        break
    else:
        print("Invaild value, can't proceed...")
        count -= 1
    







