import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=['!','#','$','%','&','(',')','*','+']
print("Welcome to the pypassword generator!")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_symbols=int(input("How many symbols would yo like?\n"))
nr_numbers=int(input("How many numbers would you like in your password?\n"))
list=[]
for char in range(0,nr_letters):
    x=random.choice(letters)
    list.append(x)
for char in range(0,nr_symbols):
    list.append(random.choice(symbols))
for char in range(0,nr_numbers):
    list.append(random.choice(numbers))
y=random.shuffle(list)
print(list)
password=""
for char in list:
    password+=char
print(f"Your password is: {password}")
