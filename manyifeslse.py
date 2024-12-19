bill = 0  # Initialize bill to 0
height = int(input("Enter the height: "))

if height >= 120:
    print("You can enter.")
    
    age = int(input("Enter your age: "))
    if age <= 12:
        print("Bill is $20.")
        bill = 20
    elif age <= 18:  # age condition for teenagers
        print("Bill is $25.")
        bill = 25
    else:  # Adults 
        print("Bill is $30.")
        bill = 30

    want_tip = input("If you want to add a tip, press Y or N: ").upper()  # .upper() to handle both 'y' and 'Y'
    if want_tip == "Y":
        bill += 3  # Add $3 as a tip
        
    print("Your total bill is: $", bill)  # Correct syntax for print statement
else:
    print("You cannot enter.")
