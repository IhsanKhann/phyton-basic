import json

# Define Members class
class Members:
    def __init__(self, name, age, education):
        self.name = name
        self.age = age
        self.education = education

    def __str__(self):  # display
        return f"Name: {self.name} Age: {self.age} Education: {self.education}" 

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "education": self.education
        }

    @classmethod
    def from_dict(cls, data):  # this data is a dictionary
        return cls(data["name"], data["age"], data["education"])


# Define Books class
class Books:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title} Author: {self.author} Year: {self.year}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["year"])


# Define Library class
class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def save_data(self):
        with open("members.json", "w") as file:
            json.dump([member.to_dict() for member in self.members], file, indent=4)

        with open("books.json", "w") as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def load_data(self):
        try:
            with open("members.json", "r") as file:
                data = json.load(file)
                self.members = [Members.from_dict(member) for member in data]
        except:
            self.members = []

        try:
            with open("books.json", "r") as file:
                data = json.load(file)
                self.books = [Books.from_dict(book) for book in data]
        except:
            self.books = []

    def addBook(self, book):
        for b in self.books:
            if b.title == book.title:
                print("Duplicate book found.")
                return
        self.books.append(book)
        self.save_data()
        print("Book added successfully.")

    def deleteBook(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                self.save_data()
                print(f"Book '{title}' removed.")
                return
        print("Book not found.")

    def addMember(self, member):
        for m in self.members:
            if m.name == member.name:
                print("Duplicate member found.")
                return
        self.members.append(member)
        self.save_data()
        print("Member added successfully.")

    def deleteMember(self, name):
        for member in self.members:
            if member.name == name:
                self.members.remove(member)
                self.save_data()
                print(f"Member '{name}' removed.")
                return
        print("Member not found.")

    def displayBooks(self):
        print("Books in Library:")
        for book in self.books:
            print(book)

    def displayMembers(self):
        print("Members in Library:")
        for member in self.members:
            print(member)

# Main function
def main():
    lib = Library()

    while True:
        print("\n=== Library Management ===")
        print("1 - Add")
        print("2 - Delete")
        print("3 - Display")
        print("4 - Exit")

        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                option = int(input("1 - Add Member, 2 - Add Book: "))
                if option == 1:
                    name = input("Enter name: ")
                    age = input("Enter age: ")
                    education = input("Enter education: ")
                    member = Members(name, age, education)
                    lib.addMember(member)
                elif option == 2:
                    title = input("Enter book title: ")
                    author = input("Enter author: ")
                    year = input("Enter year: ")
                    book = Books(title, author, year)
                    lib.addBook(book)
                else:
                    print("Invalid option.")

            elif choice == 2:
                option = int(input("1 - Delete Member, 2 - Delete Book: "))
                if option == 1:
                    name = input("Enter member name to delete: ")
                    lib.deleteMember(name)
                elif option == 2:
                    title = input("Enter book title to delete: ")
                    lib.deleteBook(title)
                else:
                    print("Invalid option.")

            elif choice == 3:
                option = int(input("1 - Display Members, 2 - Display Books: "))
                if option == 1:
                    lib.displayMembers()
                elif option == 2:
                    lib.displayBooks()
                else:
                    print("Invalid option.")

            elif choice == 4:
                print("Exiting program.")
                break
            else:
                 print("Invalid choice. Please try again.")
        except ValueError:
            print("Please choose the correct options.")
        except TypeError:
            print("Please enter an int value")
        except Exception:
            print("An error occured.")
          
# Run main
main()
