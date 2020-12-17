"""
Written By Shaharyar Ahmed
"""
from os import system
from time import sleep

#Main program loop
while True:
    #Exception handling
    try:
        #Getting user input
        num_1 = int(input("Enter A Number: "))
        num_2 = int(input("Enter A Another Number: "))
        operation = input("Enter A Operation e.g: (+ , - , / , *) or type it in e.g: 'add' , 'subtract': ")

    except Exception as e:
        print("Please Type In A Number Not A String")
    
    #Checking what the operation is
    if operation == "+" or "add" in operation.lower():
        result = num_1 + num_2
        print(f"{num_1} + {num_2} = {result}")

    elif operation == "-" or "sub" in operation.lower():
        result = num_1 - num_2
        print(f"{num_1} - {num_2} = {result}")

    elif operation == "*" or "mul" in operation.lower():
        result = num_1 * num_2
        print(f"{num_1} * {num_2} = {result}")

    elif operation == "/" or "div" in operation.lower():
        result = num_1 / num_2
        print(f"{num_1} / {num_2} = {result}")

    else:
        print("Operation Not Supported Yet!")
    
    #Clearing the screen
    sleep(2)
    system("cls")
