from room import mid_range_rooms, semi_luxury_rooms, premium_rooms
from menu import chicken_meal , chinese_menu , drink_menu , rice_meal

print("***********************")
print("Welcome to PY HOTELS")
print("***********************")

print("Manager - How may i help you sir?\n1- Want a room\n2- Dine at restaurant\n3- Exit")
class hotelroom():
    def room(self , n):
        self.n = n
        print("Manager- Will you be staying overnight, or is this for a One day?\n1- One day\n2- One night\n3- Few hours only")
    def shift(self , n):
        self.n = n
        print("**Here our list**")
        for room_no, room_data in mid_range_rooms.items(): #actually we are in nested dict so we have to do this try of logic for "for loop"
            print(f"Room no-{room_no} which is {room_data['category']} and its rent is {room_data['rent_per_day']}/-")
        print("Manager: select which rooms you want.")

    def select(self , n):
        self.n = n
        room_data = mid_range_rooms[q]
        print(f"Thanks sir for booking room no {q}! Here is your bill:\nRoom type: {room_data['category']}\nRoom rent: {room_data['rent_per_day']}")
        

a = hotelroom()
x = int(input("Choose your option from above: "))
print("")
a.room(x)
b = int(input("Enter your opinion: "))
a.shift(b)
q = int(input("select room: "))
a.select(q)