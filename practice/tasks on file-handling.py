f = open("Quote.txt", "w")
f.write("Become a Warrior in a World of Worries")
f.close()

# Task-2
f = open("Quote.txt", "a")
f.write(" Be Crazy")
f.close()

# Task-3
f = open("Quote.txt", "r")
print(f.readlines())  # Reads all lines
f.close()

# Task-4: Appending explanation
f = open("Quote.txt", "a")
f.write(" 24 bytes in C++, in Python more - because a string is an object with hash values, characters, pointer etc etc ")
f.write(" and everything takes size so it almost takes the string size to '49 bytes', 1 byte is taken by one character.")
f.close()

# Task-5: Reading with sizehint
f = open("Quote.txt", "r")
print("Specific size:", f.readlines(1))  # Reads approx 1 byte worth of lines (will likely return just the first line)
f.close()

f = open("Quote.txt", "r")
content = f.readline()
count = 0

for i in content:
    count += 1

print(f"count is: {count}")
f.close()

#Task-6:
key = input("Enter the word you want to search: ")
with open("Quote.txt") as f:
    content = f.readlines()
for i in content:
    if key in i:
        print(f" key found: {key} ")
        break
    else:
        print("not found.")

#Task-7: copy data from one file to another
with open("Quote.txt", "r") as a:
    content = a.readlines()
    #print in reverse:
    print(content[::-1])

with open("CopiedQuote.txt", "w") as a: 
    a.writelines(content)


# 9. Word Frequency
# Read a file
# Count how many times each word appears
# Print the result (like a mini dictionary).

#1- split all the sentences to indiviual words and then I would make a set out of it. So list to set to list
#2- count method to count all the elements and then store that count in another list. Use append for it.
#3- take these 2 lists and make a dictionary of it. (Word:count)
#4- print it out

with open("Quote.txt", "r") as I:
    content = I.readlines()

split_words = [i.split() for i in content] # split every sentence to inidiviual words
content = sum(split_words, []) # this is for converting a nested list to a normal list.

count = []
for i in content:
    x = content.count(i)
    count.append(x)

Remove_Duplicates = set(content) # convert the list to a set with no duplicates.
words = list(Remove_Duplicates)
Data = dict(zip(words,count))

for key,value in Data.items():
    print(f" {key} : {value} ")
    








# 🔴 Advanced Tasks
# 10. Remove Blank Lines
# Read a file

# Create a new file that contains the same content without blank lines.

# 11. Sort File Lines Alphabetically
# Read all lines of a file

# Sort them

# Write them into a new file sorted.txt.

# 12. Merge Two Files
# Read from file1.txt and file2.txt

# Combine their contents into merged.txt.



