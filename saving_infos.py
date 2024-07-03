import json as js
import time
fname = str(input("Type First Name: "))
lname = str(input("Type Last Name: "))
age = str(input("Type Age: "))
height = str(input("Type Height: "))
weight = str(input("Type Weight: "))
married = str(input("Type True or False: "))
z = int(input("Type the Year: "))
y_all = 0
code = fname[0:2]+lname[2:5]+age+height+weight+married[0]
class info_civi():
    def personal_inf():
        print(f"Code: {code}")
    def expire_Date():
        global y_all
        if int(age)>=18:
            y=0
            y_all = y
        elif int(age)<=13:
            x = int(age)
            w = 13
            y = w+z-x
            y_all = y
        else:
            x = int(age)
            w = 18
            y = w+z-x
            y_all = y
        print(f"Expire Date: {y}")
    def saving_inf():
        inf = {
            'First_Name': fname, 
            'Last_Name': lname, 
            'Age': age,
            'Height': height, 
            'Weight': weight, 
            'Married': married,
            'Expire Date': y_all
        }
        with open(f"saves_inf/{code}.json", "w") as save_file:
           js.dump(inf, save_file, indent=6)
        save_file.close()
info_civi.personal_inf()
info_civi.expire_Date()
print("     Saving The Informations...    ")
info_civi.saving_inf()
time.sleep(2.5)
print("Done")
input("press any key to exit...")