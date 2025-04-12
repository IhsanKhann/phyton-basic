import json

Books = []
Book_Count = 0
Max_count = 100

def Load_Books():
    global Books, Book_Count
    try:
        with open("Library.json", "r") as file:
            Books = json.load(file)
            Book_Count = len(Books)
            print("Books loaded successfully.")
    except FileNotFoundError:
        Books = []
        Book_Count = 0
        print("Library file not found. Starting fresh.")

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

class Library:
    def __init__(self):
        self.books = []

    def Append_Books(self, book):
        global Max_count, Book_Count
        if Book_Count < Max_count:
            self.books.append(book)
            Append_Books(book)
            Book_Count += 1
            print("Book added successfully.")
        else:
            print("Library is full. Cannot add more books.")

    def View_Books(self):
        if not Books:
            print("No books available.")
            return
        for book in Books:
            print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, ID: {book['id']}")

    def Search_Book(self):
        title = input("Enter book title to search: ")
        for book in Books:
            if book["title"] == title:
                print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, ID: {book['id']}")
                print("Book found.")
                return
        print("Book not found.")

    def Remove_Books(self, title):
        found = False
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                Delete_books(title)
                found = True
                break
        if not found:
            print("Book couldn't be removed / Not Found.")

def main():
    Load_Books()
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            try:
                id = int(input("Enter book ID: "))
                book = Book(title, author, genre, id)
                library.Append_Books(book)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '2':
            library.View_Books()
        elif choice == '3':
            library.Search_Book()
        elif choice == '4':
            title = input("Enter book title to delete: ")
            library.Remove_Books(title)
        elif choice == '5':
            print("Exiting...")
            Save_Books()
            break
        else:
            print("Invalid choice. Please try again.")

# Run the system
main()
