#Rock,Paper and Scissors:
#User choice:
import random
choice = int(input("Enter your choice: 1,2,3 "))
if (choice == 1):
    print("Rock")
elif(choice == 2):
    print("Paper")
elif(choice == 3):
    print("Scissors")
else:
    print("Wrong choice.")
#Computer Choice:
comp_choice = random.randint(1,3)
if(comp_choice == 1):
    print("Computer Choice: Paper")
elif(comp_choice == 2):
    print("Computer Choice: Scissors.")
else:
    print("Computer Choice:Rock")
    
if(choice == comp_choice):
    print("You lose and the computer win.") 
else:
    print("You Win and the computer lost.")