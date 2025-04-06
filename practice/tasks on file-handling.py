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


# 9. Word Frequeny:
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

#Task-10: 
with open("Quote.txt", "r") as r:
    lines = r.readlines() #reading

with open("QuoteNew.txt", "w") as w: #writing
    for line in lines:
        if line.strip():
            w.write(line)



