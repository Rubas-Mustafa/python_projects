# define the function needed : operations
# print option to the user
# ask for values
# call the values
# while loop to continue the program until user wants to exit

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + "=" + str(answer))

def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + "=" + str(answer))

def mult(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + "=" + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + "=" + str(answer))

while True: 
    print("B. Subtract")
    print("C. Multiply")
    print("D. Divide")
    print("A. Addition")
    print("E. Exit")

    operation = input("Enter the Arthmetic Operation: ")

    if operation == "A":
        print("Addition")
        a = int(input("Enter the first Number: "))
        b = int(input("Enter the Second Number: "))
        add(a, b)
    elif operation == "B":
        print("Subtarction")
        a = int(input("Enter the first Number: "))
        b = int(input("Enter the Second Number: "))
        sub(a, b)
    elif operation == "C":
        print("Multiplication")
        a = int(input("Enter the first Number: : "))
        b = int(input("Enter the Second Number: "))
        mult(a, b)
    elif operation == "D" :
        print("Division")
        a = int(input("Enter the first Number: "))
        b = int(input("Enter the Second Number: "))
        div(a, b)
    elif operation == "E":
        print("Exit the program")
        quit()
