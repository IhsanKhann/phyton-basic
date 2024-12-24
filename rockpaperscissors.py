print ("Welcome to the game of Rock, Paper and Scissors.")
import random
my_choice = int(input("Chooce 0 for Rock, Choose 1 for Paper and Choose 2 for Scissors."))
comp_choice = random.randint(0,2)

choices = ["Rock","Paper","Scissors"]
print (f"Your Choice: {choices[my_choice]}  ")
print (f"Comp Choice: {choices[comp_choice]}")

if my_choice == comp_choice:
    print("draw")
elif(my_choice == 0) and (comp_choice == 2) or \
    (my_choice == 1) and (comp_choice == 0) or \
    (my_choice == 2) and (comp_choice == 1):
        print("You win.")
else:
    print("You lose!")
