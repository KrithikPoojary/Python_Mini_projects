#basic two operation calculator


print("1- Addition\n2- Subtraction\n3- Multiplication\n4- Division\n5- Average\n6- Square\n7- Cube\n8- Square root")

#All functions for following operation
def add(num1 , num2):
    return num1 + num2
def sub(num1 , num2):
    return num1 - num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def avg(num1 , num2):
    return (num1+num2)/2
def sq(num):
    return num*num
def cube(num):
    return num*num*num
def square_root(num):
    return num**(1/2)
print("") #This print is for just space

user = int(input("Select the following number to use operation: ")) #user will choose his operation
if user==1:
    number1 = float(input("Enter the number1: "))
    number2 = float(input("Enter the number2: "))
    print(f"{number1} + {number2} = {add(number1 , number2)}")

elif user==2:
    number1 = float(input("Enter the number1: "))
    number2 = float(input("Enter the number2: "))
    print(f"{number1} - {number2} = {sub(number1 , number2)}")

elif user==3:
    number1 = float(input("Enter the number1: "))
    number2 = float(input("Enter the number2: "))
    print(f"{number1} X {number2} = {mul(number1 , number2)}")

elif user ==4:
    number1 = float(input("Enter the number1: "))
    number2 = float(input("Enter the number2: "))
    if number2==0:  #Handles 0 for division
        print("divisor cannot be zero!!")
    else:
        print(f"{number1} / {number2} = {div(number1, number2)}")

elif user==5:
    number1 = float(input("Enter the number1: "))
    number2 = float(input("Enter the number2: "))
    print(f"The average of {number1} and {number2} is {avg(number1,number2)}")

elif user==6:
    number = float(input("Select the number you want to square: "))
    print(f"The square of {number} is {sq(number)}")

elif user==7:
    number = float(input("Select the number you want to cube: "))
    print(f"The cube of {number} is {cube(number)}")

elif user ==8:
    number = float(input("Select the number to find its square_root: "))
    if number < 0:
        print("Negative number is not allowed")  #Handle negative numbers for square_root
    else:
        print(f"The square_root of {number} is {square_root(number)}")

else:
    print("Invalid choice! Please select a number between 1 and 8.")