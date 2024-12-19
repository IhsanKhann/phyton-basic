print("Your Love score is being calculated....")
name1 = input("Enter the first name")
name2 = input("Enter the 2nd name") 
combined_name = name1 + name2 
lower_names = combined_name.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
first_digit = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
second_digit = l + o + v + e

score = str(first_digit) + str(second_digit)
# the score is stored as string 
score = int(score)
if (score <= 10) or (score >= 90):
    print("You guys get together really really well.")
elif(score >=40) and (score <= 50):
    print("You guys just get together alright.")
else:
    print(f"The score {score} is just alright.")





