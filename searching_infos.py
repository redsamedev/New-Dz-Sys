import os
import json as js
data = None
def searching():
    code_to_search = input("Type Code: ")
    saves_dir = os.listdir(path='saves_inf/')
    fixed_code_input = f'{code_to_search}.json'
    if fixed_code_input in saves_dir:
        with open(f'saves_inf/{fixed_code_input}', "r") as inf_file:
            data = js.load(inf_file)
            Fname = data["First_Name"]
            Lname = data["Last_Name"]
            Age = data["Age"]
            Height = data["Height"]
            Weight = data["Weight"] 
            Married = data["Married"]
            ExpireDate = data["Expire Date"]
            data_list = [f'First Name: {Fname}', f'Last Name: {Lname}', f'Age: {Age}', f'Height: {Height}', f'Weight: {Weight}', f'Married: {Married}', f'Expire Date: {ExpireDate}']
            for i in data_list:
                print(i)
    else:
        print(f'theres no file called{code_to_search}')
searching()
input("press any key to exit...")
