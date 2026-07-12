from room import mid_range_rooms, semi_luxury_rooms, premium_rooms
from menu import chicken_meal , chinese_menu , drink_menu , rice_meal
from datetime import datetime
now = datetime.now()
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
        b = now.strftime("%Y-%m-%d %H:%M:%S")
        room_data = mid_range_rooms[n]
        print(f"Thanks sir for booking room no {n}! Here is your bill:\nRoom type: {room_data['category']}\nRoom rent: {room_data['rent_per_day']}\nCheck in time = {b}")

full_menu = {**chinese_menu, **rice_meal, **chicken_meal, **drink_menu}  #The ** here is called dictionary unpacking.

class hotel_restaurant():
    def __init__(self):
        self.orders = []

    def table(self, n):
        self.n = n
        print("Manager : Welcome sir! Here is dining room\n")
        if n == 2:
            print("**MENU**")
            print(" *************CHINESE MENU********** ")
            for menu_no1, menu_data1 in chinese_menu.items():
                print(f"Order_no:{menu_no1}- {menu_data1['name']}\n Price= {menu_data1['price']}rs")
            print("*************RICE MEAL MENU**********")
            for menu_no2, menu_data2 in rice_meal.items():
                print(f"Order_no:{menu_no2}- {menu_data2['name']}\n Price= {menu_data2['price']}rs")
            print("*************CHICKEN MEAL MENU**********")
            for menu_no3, menu_data3 in chicken_meal.items():
                print(f"Order_no:{menu_no3}- {menu_data3['name']}\n Price= {menu_data3['price']}rs")
            print("*********DRINK MENU*******")
            for menu_no4, menu_data4 in drink_menu.items():
                print(f"Order_no:{menu_no4}- {menu_data4['name']}\n Price= {menu_data4['price']}rs")
            print("Manager: Any order sir?.")

    def order(self):
        while True:
            n = int(input("Enter Order_no to order: "))
            if n not in full_menu:
                print("Invalid Order_no, try again.")
                continue

            qty = int(input(f"How many {full_menu[n]['name']} would you like? "))
            item = full_menu[n]
            subtotal = item['price'] * qty

            self.orders.append({
                "name": item['name'],
                "price": item['price'],
                "qty": qty,
                "subtotal": subtotal
            })

            more = input("Order more items? (y/n): ").lower()
            if more != 'y':
                break

    def bill(self):
        print("\n********** YOUR BILL **********")
        grand_total = 0
        for item in self.orders:
            print(f"{item['name']} x{item['qty']} @ {item['price']}rs = {item['subtotal']}rs")
            grand_total += item['subtotal']
        print(f"--------------------------------")
        print(f"Grand Total: {grand_total}rs")
        print(f"Checkout time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print("********************************")






a = hotelroom()
b = hotel_restaurant()
x = int(input("Choose your option from above: "))
if x == 1:
    print("")
    a.room(x)
    b_choice = int(input("Enter your opinion: "))
    a.shift(b_choice)
    q = int(input("select room: "))
    a.select(q)
elif x == 2:
    b.table(x)
    b.order()   # no longer takes n — it loops internally now
    b.bill()    # prints the final itemized bill
elif x == 3:
    pass
