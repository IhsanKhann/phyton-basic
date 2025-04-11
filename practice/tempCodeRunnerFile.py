# Library Managament System:
import json

Books = []

def Load_Books():
    global Books

    with open("Library.json", "r") as file:
        Books = json.load(file)
        print("Books loaded successfully.")


def Save_Books():
    with open("Library.json", "w") as file:
        json.dump(Books, file, indent=4)  
        print("Books saved successfully.")


def Append_Books(book):

    Converted_book = book.convert()

    Books.append(Converted_book)
    Save_Books()

class Book:
    def __init__(self,title,author,genre,id):
        self.title = title
        self.author = author
        self.genre = genre
        self.id = id    

    def __str__(self):
        return (f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, ID: {self.id}")

    def convert(self):
        converted_Book = {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "id": self.id
        }
        return converted_Book
    
class Library:
    pass

def main():
    # load the books as soon as the program starts
    Load_Books() 

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1)
    Append_Books(book1)

# calling main
main() 
