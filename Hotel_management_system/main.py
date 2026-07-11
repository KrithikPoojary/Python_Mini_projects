from room import mid_range_rooms, semi_luxury_rooms, premium_rooms
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
            print("Manager: Most welcome sir! We have Three Types of rooms Available\n1- Mid range rooms\n2- Semi_luxury_rooms\n3- premium_rooms \n4- Exit\nWhich Type of room you want sir?")
            while True:
                a = int(input("Choose room type: "))
                if a == 1:
                    print("Manager- Will you be staying overnight, or is this for a One day?\n1- One day\n2- One night\n3- Few hours only")
                    while True:
                        b = int(input("Enter your opinion: "))
                        if b == 1:
                            print("**Here our list**")
                            for room_no, room_data in mid_range_rooms.items(): #actually we are in nested dict so we have to do this try of logic for "for loop"
                                print(f"Room no-{room_no} which is {room_data['category']} and its rent is {room_data['rent_per_day']}/-")
                        print("Manager: select which rooms you want.")
                        q = int(input("select rooms: "))
                        room_data = mid_range_rooms[q]
                        print(f"Thanks sir for booking room no {q}! Here is your bill:\nRoom type: {room_data['category']}\nRoom rent: {room_data['rent_per_day']}")
                        
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
print("")
print("")
print("")