City_Pakistan = ["Islamabad" , "Karachi" , "Lahore", "Peshawar", "Gujranwala", "Faislabad", "Quetta" , 10 , 45.6 , 1 , "Ihsan Khan"]
City_Pakistan.append(20) #only add one element.
City_Pakistan.append("Muhammad") # to add another you gonna use another .append() 
City_Pakistan.extend(["Wah Cant, Pindi, Bye"])
print(City_Pakistan[(0)])
City_Pakistan.insert("HI") #adds an element in the start, only add one element at start.
print(City_Pakistan)

#list is a DataStructure.
#.append() will add an element in the end.
# you cannot add one element twice.
#you can store any kind of data in it.
#you can use .extend() to add a list at the end of a list.
