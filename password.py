#steps: 1- Take input of how many charachters do you wanna add..store it in a variable.
#2- Take input of the symbols and store it
#3- Take input of the numbers,alphabets and store it
#4- Store the symbols, numbers, alphabets into a seperate variable.
#5- The variable name is Password. Give spaces using..""
#6- assign random symbols,numbers, alphabets to the password variable. (use loop for this purpose..store random values using a loop)
#7- Print the Password.
#make a list..

import random
symbols = ['!','@','#','$','%','^','&','*','(',')']
chrachters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
#take input..
num_symbols = int(input("Number of symbols: "))
num_chrachters = int(input("Number of chrachters:"))
num_numbers = int(input("Number of numbers:"))
#password-variable:
password = "" #empty variable:

for i in range(1,num_symbols+1): 
  password = password + random.choice(symbols) #random.choice is used for choosing a random element in the list symbols.

for i in range(1,num_chrachters+1): 
  password = password + random.choice(chrachters)

for i in range(1,num_numbers+1):
  password = password + random.choice(numbers)

print (password)




