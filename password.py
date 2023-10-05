# project number #### 9

# ask user if you want to generate a passord or not
# if yes ask for password length
# generate password
# print password
# if initial no then exit the program 

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%&*()")
def generate():
    password_length = int(input("Length of password: "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password) 

    password = "".join(password)

    print(password)
# generate()

option = input("Do you want it or not: ")

if option == "Yes":
    # print(required_password)
    generate()
elif option == "No":
    print("Program Ended")
    quit()
else:
    print("Invalid Type the length of the password")