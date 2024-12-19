print ("Welcome to Treasure World.")
print("Your mission is to find the treasure.")

choice1 = input("Choose left or right.")
if (choice1 == "right"): 
    print("Game Over.")
elif (choice1 == "left"):
    choice2 = input("Do you want to swim or wait")
    if(choice2 == "swim"):
        print("Game Over.")
    elif(choice2 == "wait"):
        choice3 = input("Which Door. Red,Blue or Yellow")
        if(choice3 == "Red"):
            print("Game Over.")
        elif(choice3 == "Blue"):
            print("Game Over.")
        elif(choice3 == "Yellow"):
            print("You Won.")
        else:
            print("Invalid Choice.")