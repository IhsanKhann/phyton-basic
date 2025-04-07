import csv
import json
import pickle

#There are 2 types of data:
# 1- Human-Readble-Form: .csv, .json, .txt, .html
# 2- Binary-Form: .bin, .exe, .jpg, .png, .mp4, .mp3

# csv is used for stroing data in tbales. 
# json is used for stroing data such as lists, dictionaries etc
# similarly .bin, .exe for binary, .mp3, .mp4 for audio and video files.
# .jpg, .png for images.

#csv is the data which is stored in tabular form and data is seperated by commas
# the data is in rows and each row represent some record
# e.g: Name,City,Phone
# Ihsan,Peshawar,xXXXXXXXXXX
# csv module is used for reading and writing csv data.

#JSV: used for stroing nested structure data, such as dictionatries and other complex data structures such as trees and linked lists.
# Jsv module is used for reading and writing jsv data.

#Using csv module:
# with open("data.csv" , "w" ) as file: or
with open("data.csv", "w", newline="") as file: #ensrue that the data is written without leaving any lines.
    writer = csv.writer(file) #calls the writer method
    writer.writerow(["Name","Age","City"])
    writer.writerow(["Ihsan","19","Peshawar"])
    writer.writerow(["Ali","20","Karachi"])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)
   
with open("industry.csv", "a", newline="") as file:
    data = csv.writer(file)
    data.writerow(["HBK","Cheezious"]) 
# this will append the data 

data = [
    ["Name","Age","City"],
    ["Ihsan","19","Peshawar"],
    ["Usman","20","Karachi"]
]

#Manually open the file:
file = open("new2.csv","w",newline="") 
writer = csv.writer(file)
writer.writerows(data) #writes all the data at once because its writer.writerows()
file.close() #Manually close the file

# with open("industry.csv", "r") as file:
#     data = csv.csv.reader(file)
#     next(data) #skip the first line - of this data - that we have loaded..
#     for line in data:
#         print(line)

#csv.reader(),       csv.writer() 
# using for loop     data.writerow(one single line,row), data.writerows(insert the whole list,dictinonary),  

#using csv.DictReader() and DictWriter()
# Make an object for this then use it - it takes two parameters - file_name and then the fieldnames - the first line
data = [
    {"Name": "Ihsan", "Age": 19, "City": "Peshawar"},
    {"Name": "Usman", "Age": 20, "City": "Islamabad"},
    {"Name": "Lala", "Age": 23, "City": "Lahore"}
]

# Writing to the CSV file
with open("industry.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
    writer.writeheader() 
    writer.writerows(data)  

# Reading from the CSV file
with open("industry.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Headers:", reader.fieldnames)  
    for line in reader:
        print(line)

data = {
    "Name":"Ihsan",
    "Age":19,
    "City":"Peshawar" 
}

#using the json module:
# If data is complex, then we use serialization and de-serialization to store the data in bytes by bytes in binary form.
# json uses serializtion and de-serialization.

with open("data.json", "w") as file:
    json.dump(data,file) #data loaded into the file.

#read the data:
with open("data.json", "r") as file:
    print(json.load(file)) #loaded all the data to the file

#Binary Data:
#.bin - it has many modes such as
# rb - read in binary
# wb - write in binary
# ab - append in binary
# there are many more modes such as rb+, wb+, ab+ etc

with open("data.bin", "wb" ) as file:
    file.write(b"This is Ihsan") 

with open("data.bin", "rb") as file:
    data = file.read() 
    print(data) 

with open("data.bin", "ab" ) as file:
    file.write(b"This is Usman now")

with open("data.bin", "rb+" ) as file:
    content = file.read()
    print(content)

    file.write(b"This is sibling no-2") # file-pointer is one byte forward
    print(file.read()) # shows empty.

    file.seek(0) # moves back to the inital - start of the file.
    print(file.read()) 

#Serialization and De-serialization:
# Serialization is the process of converting complex data into the binary form.
# List,Dictionary - to binary form.

# De-serialization is the process of converting the binary data back to the original form
# Binary form back to list,dictionary.

#we use the pickle module for this. .pkl is the extension for saving the file.
# pickle.dumb() - this must be a class level method
# same goes for pickle.load() - this is also a class level method.

#   pickle.dumb() - this is used for writing the data
#   pickle.load() - this is used for reading the data.

# binary read and write modes must be used.

data = { #data is a object - .dump() converts it to binary form.
    "Name":"Ihsan" ,
    "Age":19,
    "Subject":{
        "Subject1": "Python" ,
        "Subject2": "Java" ,
        "Subject3": "C++" ,
    }
}

with open("new3.pkl", "wb") as file:
    pickle.dump(data, file) 

with open("new3.pkl", "rb") as file:
    content = pickle.load(file)
    
    for key,value in content.items():
        print(f"{key} : {value}") 

