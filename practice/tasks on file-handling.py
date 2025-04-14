import os

# f = open("Quote.txt", "w")
# f.write("Become a Warrior in a World of Worries")
# f.close()

# # Task-2
# f = open("Quote.txt", "a")
# f.write(" Be Crazy")
# f.close()

# # Task-3
# f = open("Quote.txt", "r")
# print(f.readlines())  # Reads all lines
# f.close()

# # Task-4: Appending explanation
# f = open("Quote.txt", "a")
# f.write(" 24 bytes in C++, in Python more - because a string is an object with hash values, characters, pointer etc etc ")
# f.write(" and everything takes size so it almost takes the string size to '49 bytes', 1 byte is taken by one character.")
# f.close()

# # Task-5: Reading with sizehint
# f = open("Quote.txt", "r")
# print("Specific size:", f.readlines(1))  # Reads approx 1 byte worth of lines (will likely return just the first line)
# f.close()

# f = open("Quote.txt", "r")
# content = f.readline()
# count = 0

# for i in content:
#     count += 1

# print(f"count is: {count}")
# f.close()

# #Task-6:
# key = input("Enter the word you want to search: ")
# with open("Quote.txt") as f:
#     content = f.readlines()
# for i in content:
#     if key in i:
#         print(f" key found: {key} ")
#         break
#     else:
#         print("not found.")

# #Task-7: copy data from one file to another
# with open("Quote.txt", "r") as a:
#     content = a.readlines()
#     #print in reverse:
#     print(content[::-1])

# with open("CopiedQuote.txt", "w") as a: 
#     a.writelines(content)


# # 9. Word Frequeny:
# with open("Quote.txt", "r") as I:
#     content = I.readlines()

# split_words = [i.split() for i in content] # split every sentence to inidiviual words
# content = sum(split_words, []) # this is for converting a nested list to a normal list.

# count = []
# for i in content:
#     x = content.count(i)
#     count.append(x)

# Remove_Duplicates = set(content) # convert the list to a set with no duplicates.
# words = list(Remove_Duplicates)

# Data = dict(zip(words,count))
# for key,value in Data.items():
#     print(f" {key} : {value} ")

# #Task-10: 
# with open("Quote.txt", "r") as r:
#     lines = r.readlines() #reading

# with open("QuoteNew.txt", "w") as w: #writing
#     for line in lines:
#         if line.strip():
#             w.write(line)


#Exception-Handling + File-Handling:
# 1- 
File_Info = input("Enter the file name: ")
try:
    with open(File_Info, "r") as File:
        File.readlines()
except FileNotFoundError:
    print("File not Found.")
else:
    print("File Found.")

#2-
try:
    with open(File_Info) as File:
        File.write("Hello")
except PermissionError:
    print(f"Permission for {File_Info} not granted. Sorry")
except FileNotFoundError:
    print("File not Found")
else:
    print("File Found.")

#3-
# Ask user to choose: Read, Write, or Delete
# Ask for a filename
# Use appropriate try...except logic to perform and handle each operation safely

choice = input("Choose - Read / Write / Delete: ").lower()
file_info = input("Enter file name: ")

options = ["read", "write", "delete"]

try:
    if choice == options[0]:  # Read
        with open(file_info, "r") as file:
            content = file.read()
            print("\n File Content:\n", content)

    elif choice == options[1]:  # Write
        with open(file_info, "w") as file:  # You must open in write mode
            file.write("Hello world\n")     # Fixed: .write(), not .writeline()

        print("Written to file.")

    elif choice == options[2]:  # Delete
        os.remove(file_info)
        print(" File deleted successfully.")

    else:
        raise ValueError("Invalid operation selected.")

except ValueError:
    print("Choose a correct option: read / write / delete.")
except PermissionError:
    print("Permission not granted.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Unexpected error: {e}")
    