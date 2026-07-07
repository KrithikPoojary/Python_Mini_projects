from room import rooms
from menu import chicken_meal , chinese_menu , drink_menu , rice_meal

print("***********************")
print("Welcome to PY HOTELS")
print("***********************")

print("Manager - How may i help you sir?\n1- Want a room\n2- Dine at restaurant\n3- Exit")

def book():
    pass
def dine():
    pass

while True:
    user= int(input("Choose your option from above: "))
    while True:
        if user == 1:
            book()
            exit()
        elif user == 2:
            dine()
            exit()
        elif user == 3:
            print("Thanks")
            exit()
        else:
            print("Choose between 1to3 only")
            break