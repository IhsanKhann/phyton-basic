#Practice prob-1
temp = int(input("Enter temp: "))

if temp >= 40: 
    print("Temperature is Hot.")
    humdidity = int(input("Enter humdidity: "))
    
    if humdidity >= 10:
        print ("Humid.")
    else: 
        print ("Not Humid.")
else:
    print ("Temp is less.")
    
# Grading:
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <=100: 
    print("Grade A+")
elif marks >= 80 and marks<90 :
    print("Grade A")
elif marks >= 60 and marks< 80:
    print("Grade B")
elif marks >=40 and marks<60:
    print("Grade C")
else:
    print("Grade D.")
    
#leap year: 
year = int(input("Enter a year: "))

if(year % 4 == 0):
    print("it is a leap year")
    if(year % 400 == 0):
        print("it is a leap year")
        if(year & 100 == 0):
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is not a leap year.")
else:
    print("it is not a leap year.") 
    