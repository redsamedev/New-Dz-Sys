import os
def main():
    print("sh: searching\nsv_infs: saving person infos")
    user = input("Type_Command: ") #User Input
    if user == "sh":
        os.system('searching_infos.exe') #starting the searching script
    elif user == "sv_infs":
        os.system('saving_infos.exe') #starting the saving script
    else:
        print("Command not Available")

while True:
    main()