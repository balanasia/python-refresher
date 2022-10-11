# return statement = Function send Python values/objects back to the caller 
#                    These values/objects are known as the function's return value

operator = ""

num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))

if (isinstance(num1, int) == False) or (isinstance(num1, int) == False):
    num1 = int(input("Enter a number 1: "))
    num2 = int(input("Enter a number 2: "))

while (operator == "") or (operator != "+" or operator != "-" or operator != "*" or operator != "/"):
    operator = input("Invalid operator. Enter + - / *: ")
    if (operator == "+" or operator == "-" or operator == "*" or operator == "/"):
        break

def add(num1, num2):
    return num1 + num2

def diff(num1,num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 + num2

def divide(num1, num2):
    return num1 / num2

if "+" in operator:
    print(str(num1) + " + " + str(num2) + " is " + str(add(num1,num2)))
elif "-" in operator:
    print(str(num1) + " - " + str(num2) + " is " + str(diff(num1,num2)))
elif "*" in operator:
    print(str(num1) + " * " + str(num2) + " is " + str(multiply(num1,num2)))
elif "/" in operator:
     print(str(num1) + " / " + str(num2) + " is " + str(divide(num1,num2)))
else:
    print("Invalid operation")