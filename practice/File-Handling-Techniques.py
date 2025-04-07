import os
import pathlib
import shutil

# We will cover:
# 1- Checking if a file exists ?? if the path of the file is present, 2- Remove/Delete a file or a complete folder
# (folder should be empty), 3- Renaming and moving files

# Modules/Libaries used: os, pathlib (used for checking if a path exists). 
# 1- os.path.exists() , 2- Path.exists()

# use os.mkdir() to make a folder, use os.rmdir() to remove a folder
# r"path_name" - this is called a raw(r) string which is used with paths with lots 
# of slash's ( / ).
# common error we can get is the permission_error - so use the general
# exception to catch it.
# FileFoundError in case the file is not present

# os.rename() annd shutil.move() - these 2 methods are used when we want to rename or move our file
# os.rename() - for renaming the file, takes 2 parameters: (old_file, new_file)

# shutil (module) 
# shutil.rmtree() is used to remove non-empty-folders.
# shutil.copy() for copying folders
# shutil.rmdirs() for removing folders
# shutil.mkdir() 
# shutil.rmdir() for making folder
# shutil_move() - for moving the file, takes 2  parameter: (source, destination) - source is the file name, Destination - where you want to move the file.

#Task-1: Method 1: using os
file = r"C:\Users\Ihsan\Desktop\python\phyton-basic\practice"
if os.path.exists(file): #if True
    print("Path Exists")
else:
    print("Does not Exist")

# Method-2: using try-except:
try:
    if not os.path.exists(file):
        raise FileNotFoundError("File not Found")
except FileNotFoundError as e:
    print(f"Error: {e} ")
else:
    print(f"File Found {file} ")

# Method-3: using the pathlib:
myfile = pathlib.Path(file) # correct syntax
if myfile.exists(): #myfile has data we just check it
    print("File Found")
else:
    print("File not Found.")

#Topic-2: Deleting and Removing a File.
try:
    os.remove(file) 
    print("File removed.")
except FileNotFoundError: 
    print("File couldnt be Found")
except:
    print("Error deleting the file.")

#removing a folder:
# os.mkdir("Python_Testing_Folder")
# print("Folder opened.")

# folder_target = "Python_Testing_Folder"
# os.rmdir(folder_target)
# print("Folder removed.")

#Topic-3:
#Renaming and moving a file.
old_name = "Quote.txt"
new_name = "haha.txt" 

try:
    os.rename(old_name, new_name)
    print(f"{old_name} changed to {new_name} ")

except FileNotFoundError:
    print("File not Found.")
except Exception as E:
    print(f"Error: {e}")

#moving a file to another destination:
#shutil.move() is used
# shutil.move("haha.txt", file)
# file = new_name
# print(f"File: {file} moved to new destination: {file}")
