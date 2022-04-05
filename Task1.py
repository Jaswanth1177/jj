import re

option = int(input("Enter 1 to New Registration 2 to Login to your account and 3 to Forget Password: \n"))

# New Registration
def register():
    store = ""
    # global store
    f = open("new.txt", "a")
    emid = input("Enter EMail id: ")
    if (validate(emid) == True):
        passwrd = input("Enter Password: ")
        if (valid(passwrd)):
            store = emid + " " + passwrd
            print("Registration Successful. Now You can Login.")
        else:
            print("Password invalid! Please try again")
            register()
    else:
        print("Mail id invalid! Please try again")
        register()

    f.write("\n")
    f.write(store)


    # print(f.readline())

#Login
def login():
    e = input("Enter Email id to login: ")
    p = input("Enter Password: ")
    sear = e + " " + p
    #f = open("new.txt", "r")
    index = 0
    flag = 0

    with open("new.txt","r") as f:
        lin = f.read().splitlines()

        if (sear in lin):
            print("Login Successful")
            #break

        else:
            v = int(input(("Invalid Login Details! or User not found! Please enter 1 to create new account or enter 2 for forget password.")))
            if(v==1):
                register()
                #break
            elif(v==2):
                forget()
                #break
            else:
                print("Entered wrong option. Please register!")
                register()

#Validating Email id
def validate(validstr):
    reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(reg, validstr)):
        return True
    else:
        return False

#Validating Password
def valid(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 16:
        print('length should be not be greater than 16')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

#Forget Password
def forget():
    x = input("Enter mail id to retrieve password: ")


    if(validate(x)==True):
        with open("new.txt","r") as s:
            lines = s.read().split()
            for i in range(len(lines)):
                if(x == lines[i]):
                    print("Your Password is " + lines[i+1])
                    break
                else:
                    print("Invalid Username! Please create new login")
                    register()
        s.close()


if (option == 1):
    register()
elif (option == 2):
    login()
elif (option == 3):
    forget()
else:
    print("You Have Entered the Wrong Option")
