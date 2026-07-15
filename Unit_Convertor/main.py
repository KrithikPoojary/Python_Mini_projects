import time

# welcome message pops 
print("****************************")
print("Welcome to Unit_convertor")
print("****************************")
time.sleep(1)
print("Here we can convert the following units like..")
print("1. CM → Inch\n2. Inch → CM\n3. KG → Pound\n4. Pound → KG\n5. KM → Mile\n6. Mile → KM\n7. Celsius → Fahrenheit\n8. Fahrenheit → Celsius")
print("")

# Working functions
def cm_inchs(n):
    i = n/2.54
    print(f"The convertion of {n}cm to Inchs is {round(i ,2 )}inchs")

def inchs_cm(n):
    cm = n*2.54
    print(f"The conversion of {n}inchs to Centimeter is {round(cm ,2)}cm")

def kg_pound(n):
    p = n*2.20462
    print(f"The conversion of {n}kg to Pounds is {round(p, 2)}lb")

def pound_kg(n):
    kg =  n*0.453592
    print(f"The conversion of {n}lb to kilograms is {round(kg,2)}kg")

def km_mile(n):
    mile = n*0.621371
    print(f"The conversion of {n}km to Miles is {round(mile,2)}miles")

def mile_km(n):
    km = n*1.60934
    print(f"The comversion of {n}miles to kilomiters is {round(km,2)}km")

def celsius_fahrenheit(n):
    far= (n*9/5)+32
    print(f"The conversion of {n}°C to Fahrenheit is {round (far ,2 )}°F")

def fahrenheit_celsius(n):
    cel = (n-32)*5/9
    print(f"The conversion of {n}°F to Celsius is {round (cel ,2 )}°C")

# Loops to satisfies the user interaction with units he want to convert

while True:
    user = int(input("For the conversion choose 1 to 8 from above units: "))

    if user ==1:
        n = int(input("Please enter value "))
        cm_inchs(n)
    elif user ==2:
        n = int(input("Please enter value "))
        inchs_cm(n)
    elif user ==3:
        n = int(input("Please enter value "))
        kg_pound(n)
    elif user ==4:
        n = int(input("Please enter value "))
        pound_kg(n)
    elif user ==5:
        n = int(input("Please enter value "))
        km_mile(n)
    elif user ==6:
        n = int(input("Please enter value "))
        mile_km(n)
    elif user ==7:
        n = int(input("Please enter value "))
        celsius_fahrenheit(n)
    elif user ==8:
        n = int(input("Please enter value "))
        fahrenheit_celsius(n)
    elif user <= 0 or user >= 8:
        print("Please select the number between 1-8 only")
        break
    else :
        print("Something went wrong! Try agin..")
        break
    while True:
        v = input("Want to convert more? [y/n]").strip().lower()
        print('')
        if v == "y":
            break
        elif v == "n":
            print("Thanks you!")
            exit()
        else:
            print("Please choose between [y/n]")
