#for calculating the average-height.
students_height = [5.6,5.7,5.4,5.9,6.1]
total_students = 0
total_height = 0
for height in students_height:
  total_height = round(total_height + height) #the height is rounded.
  
print(total_height)

for students in students_height:
    total_students = total_students+1
    
print(total_students)

average_height = total_height/total_students
print (average_heigh)