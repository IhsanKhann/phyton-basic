#now take input of students..make a list:
import random
num_std = int(input("Number of students: "))
mid_term = [0]*num_std #list will be made with n number of students with value 6.
final_term = [0]*num_std
total_marks = [0]*num_std

for i in range(0,num_std):
    mid_term[i] = random.randint(5,30)
    final_term[i] = random.randint(5,50)
    total_marks[i] = mid_term[i] + final_term[i]
    
print ("Mid term marks:", mid_term)
print ("Final term marks:", final_term)
print ("Total marks: " , total_marks)

groups = []
for _ in range(0,8):
    groups.append("") #empty string

# Grouping logic
for marks in total_marks: #iterate every element.
    if (marks >= 5 and marks <= 10):
        groups[0] += "*"
    elif (marks >= 11 and marks <= 20):
        groups[1] += "*"
    elif (marks >= 21 and marks <= 30):
        groups[2] += "*"
    elif (marks >= 31 and marks <= 40):
        groups[3] += "*"
    elif (marks >= 41 and marks <= 50):
        groups[4] += "*"
    elif (marks >= 51 and marks <= 60):
        groups[5] += "*"
    elif (marks >= 61 and marks <= 70):
        groups[6] += "*"
    elif (marks >= 71 and marks <= 80):
        groups[7] += "*"

# Print grouped asterisks
ranges = [
    "5-10", "11-20", "21-30", "31-40",
    "41-50", "51-60", "61-70", "71-80" ]

for i in range(8):
    print(f"Group {i+1} ({ranges[i]} marks): {groups[i]}")
    
    
    
    
        

    