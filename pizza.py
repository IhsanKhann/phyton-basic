print("Welcome to the pyhton pizza Deliveries.")
size = input("Enter the size 'S, M, L' ")
add_peproni = input("Do you want pepproni: Y or N ")
extra_cheese = input("Do you want cheese: Y or N")
bill = 0

if size == "S":
    bill = 100
elif size == "M":
    bill = 150
else:
    bill = 200
    
if add_peproni == "Y": 
    if size == "S":
        bill += 10
    elif size == "M":
        bill += 15
    else:
        bill += 20
else:
    print("Bill stays the same.")
    
if extra_cheese == "Y":
    bill += 1
else:
    print("Bill stays the same.")
    
print(f"Total Bill: ${bill}." )

