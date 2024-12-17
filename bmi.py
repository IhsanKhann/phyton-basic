# take height and weight input 
weight = input("Enter weight: ")
height = input("Enter height: ")

#now convert string type to int (for weight) and string to float (for height)
weight_int = int(weight)
height_float = float(height) 

# now put weight and height in formula:
bmi = weight_int/height_float * height_float # we can also do a height ** 2

#convert bmi to float:
bmi_int = int(bmi)

#display result: 
print("The BMI is: " , bmi_int)