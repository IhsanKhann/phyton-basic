#Write a program to choose that who will pay:
import random
names = ["Ihsan" , "Mowdat" , "Moeen" , "Don" , "Legend" , "Reem" , "Khamar" , "Talha" , "Waqas" , "Zohaib"  , "Saad" , "dawar"]
# choose a random person: 
totalitems = len(names)
random_name = random.randint(0, totalitems-1) # -1 because of index #this will store an index.
Person_who_will_pay = names[random_name] #an index will be stored here.
print(Person_who_will_pay) 

