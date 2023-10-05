# collect email from user
# slice the email using the @, the first part as the user name, the second part is gonna be the domain 
# split the domain using . 

def slicer():
    print("Welcome to Email Slicer: ")

    email_slicer = input("Enter your Email: ")
    (username, domain) = email_slicer.split("@")
    (domain, extension) = domain.split(".")

    print("User Name: ", username)
    print("Domain: ",domain )
    print("Extension: ", extension)

while True:
    slicer()