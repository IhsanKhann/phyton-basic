# check if number is Even/Odd: 
number = input("Enter a number: ")
if int(number) % 2 == 0:
 print("Even Number.")
else:
 print("odd number.")
 
#if else questions: 
Weather = int(input("What is the weather (in degrees)? "))

# Check if the weather is hot or chilly
if Weather >= 40:
    print("The weather is hot.")
else:
    print("The weather is chilly.")

#if else ques-2: 
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number: "))
total = num1 + num2

if total >= 100:
  print("The sum is greater than 100.")
else: 
  print("Sum is below 100.")
  
#if else bool:
isFound = False
number1 = int(input("Enter number: "))
if number1 % 2 == 0: 
 isFound = True 
else:
 isFound = False

if isFound: 
    print ("Even number Found.")
else:
    print ("Odd number.")
