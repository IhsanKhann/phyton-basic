import os
# File Handling is simple.
# File is supposed to be opened first.
# open() - opening a file, take 2 parameters(file_name, mode)

# Their are 4 modes in file-handling: r,w,x,a
# r - read - you can only read the file. Now the file is on read - mode by default is read.
# w - write - you can only write data to this file. Not write by default.
# x - create - error is given if the file pre-exists.
# a - we add more data - if a file is not created. This creates it for us as well

# data is read/written in 2 forms in python: 1-Text (Human readable form) and 2-Binary which we will be discussing further
# down the line.

# closing the file is important after the operation - abc.close() - takes no argument and file is closed.

# at the end it is very important that you delete the file.
# but you cannot close the file without a module
# you need to import os (a module) - give us methods for interacting with operating system.
# os.remove("file_name.txt") - method to remove the file
# os.path.exists(file_name.txt) - to check if the file exists - returns true,false
# os.rmdir(folder_name) - you can remove the folder - only empty folder can be removed.

# f.read() - file read using this - we can give it a parameter as well, to specify the charachters.
# f.readline() - we can read lines using this - call it once and once line is read.
# multiple lines can be read, if you call it multiple lines or if we use the
# f.readlines() method, as readlines can read multiple lines of code.

# Just like we have read(),readline(),readlines() Similarly we have the write(),writeline(),writelines() - I am pretty sure
# that the writing methods also has this one parameter(optional) i-e: sizehint. Reading methods have it no worries. Anyway
# we basically define how many bytes should you use to read/write the data. E.g 1 byte - this means that i am telling python
# use one byte of my disc to read and write this data.

#Types of data: txt (this is used for simpler purposes like: for the data that we need in human readble form). We store simple
# data structures in this form, (string, float, int) - simple primitve data-types in this form. 

# 2- we use binary (.bin) form to store images, videos and other complex data. The complex data strutures such as
# nested dictionaries, lists and tuples are stored in binary form

# Now next the question arises..how is it stored in binary. Using "serialization". 
# Now serialization is the conversion
# of storing data in bytes. De-serialization is when you convert the bytes back to txt. Its important because without it we cannot 
# store complex data. 
# serialization - json module - either convert to json.format (this is text sterialization)
# serialization - pickle module - used for converting the data to binary 

# Buffering: the process in which we read chunks of data (in bytes) or store it. The twist it that the data is first stored
# temporarily in memory and then directly to the disk. Buffering allows efficent reading and writing. The data is 
# not directly stored or written line by line or bytes by bytes which takes more time and that disk is more used.
# The Buffering provides more efficeny and performance.

# flush() is a method in which we shove all the data to the file instantly avoid buffering. All the data is written
# to the file instantly - (does instant writing)

#file pointer: tells you where you are currently in your file. File pointer is initially set at the top(beginning), then
# moves as we perform operations and move ahead. It moves bytes by bytes. Suppose i did a read(5), my pointer moved 
# 5 bytes forward.

# seek() method is used to explicity move the pointer or to reposition the pointer in the file. seek() - two parameters -
# offset, whence. Offset means how many bytes should i move.
#  seek(5, 0) - moves 5 forward - 0 means start from inital point.
#  seek(5,1)  - moves 5 forward from current position 
#  seek(5,2)  - moves 5 backward from end position.
  
# tell() method is used to determine - where the pointer stands currently. 
# with - a keyword which is used to automatically open and close the file.

# with open("file-name") as variable-name:
    # variable-name.method-name() 
# dont have to close it now - automatically closed.

