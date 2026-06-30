import random

#These are letters, numbers , symbols that give options to choice for random module
letters = ["a" , "b" , "c" , "d" ,"e" , "f" , "g" , "h" , "i" , "j" , "k" ,
"l" , "m" , "n" , "o" , "p" , "q"  , "r" , "s" ,"t" , "u" , "v" , "w" ,"x" , "y" , "z",
"A" , "B" , "C" , "D" ,  "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M",
"N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" ,"W", "X" , "Y" , "Z"]

numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]

symbols = ["!" , "@" , "#" , "$" ,"%" , "&" , "*" , "(" , ")" , "." , "-" , "+"]

print("Welcome to password Generator!!")

#User requirement
no_letter = int(input("How many letters do you want in the password:  "))
no_number = int(input("How many numbers do you want in the password: "))
no_symbol = int(input("How many symbols do you want in the password: "))

password_list = []  #For shuffle we use first List instead of String

# '_' used because there is no use of variable in for loop
for _ in range(1,no_letter+1):
    a = random.choice(letters)
    password_list.append(a)

for _ in range(1,no_number+1):
    b = random.choice(numbers)
    password_list.append(b)

for _ in range(1,no_symbol+1):
    c = random.choice(symbols)
    password_list.append(c)

random.shuffle(password_list)
password = ""  #Here String will produce the concatinated string followed by for loop and displayed 

for j in password_list:
    password += j

print(f"Here your strong password is ready: {password}\nThank you!")