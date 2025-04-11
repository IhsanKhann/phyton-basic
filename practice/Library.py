# Library Management System:
import json

Books = []
Book_Count = 0
Max_count = 100

def Load_Books():
    global Books
    global Book_Count
    global Max_count

    if  Book_Count < Max_count :
        with open("Library.json", "r") as file:
            Books = json.load(file)
            
            Book_Count = len(Books) #actually counts the number of books in the file.
            print("Books loaded successfully.")
    else:
        print("Max Limit Reached.")

def Save_Books():
    with open("Library.json", "w") as file:
        json.dump(Books, file, indent=4)  
        print("Books saved successfully.")

def Append_Books(book):
    converted_book = book.convert()
    Books.append(converted_book)
    Save_Books()
    
def Delete_books(title):
    global Books, Book_Count

    initial_count = len(Books)
    Books = [book for book in Books if book["title"] != title]
    if len(Books) < initial_count:
        Book_Count -= 1
        Save_Books()
        print("Book deleted successfully.")
    else:
        print("Book couldn't be removed. Book not found.")

class Book:
    def __init__(self, title, author, genre, id):
        self.title = title
        self.author = author
        self.genre = genre
        self.id = id    

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, ID: {self.id}"

    def convert(self):
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "id": self.id
        }
    
class Library():
    def __init__(self):
        self.books = []

    def Append_Books(self, book):
        global Max_count
        if len(self.books) < Max_count:
            self.books.append(book)
            print("Book added successfully.")
            Append_Books(book) #to append to file.
            Book_Count += 1
        else:
            print("Library is full. Cannot add more books.") 

    def View_Books(self):
        for book in Books:
           print(book)

    def Search_Book(self):
        title = input("Enter book title to search: ")
        isFound = False

        for book in Books:
            if book["title"] == title:
                isFound = True
                print(f"Title: {book['title']} Author: {book['author']} Genre: {book['genre']} Id: {book['id']}")
                break

        if isFound:
            print("Book Found")
        else:
            print("Book not Found")

    def Remove_Books(self, title):
        global Book_Count 
        isFound = False

        for book in Books:
            if title == book["title"]:
                self.books.remove(title)
                Delete_books(title)
                print("Book removed successfully.")
                break
            else:
                print("Book couldnt be removed/Not Found")
                break
def main():
    Load_Books() 
    library = Library()

    while(True):
        print("1.Add Book")
        print("2.View Books")
        print("3.Search Book")
        print("4.Delete Book")
        print("5.Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            id = int(input("Enter book ID: "))

            book = Book(title, author, genre, id)
            library.Append_Books(book)

        elif choice == 2:
            library.View_Books()
        elif choice == 3:
            library.Search_Book()
        elif choice == 4:
            title = input("Enter book title to delete: ")
            library.Remove_Books(title)
        elif choice == 5:
            print("Exiting...")
            Save_Books()
            break
        else:
            print("Invalid choice. Please try again.")
            break

# calling main
main()
