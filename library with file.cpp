#include <iostream>
#include <iomanip> // For setw
#include <string>
#include <fstream> // For file handling
using namespace std;

void saveToFile(const string titles[], const string authors[], const string genres[], const bool availability[], int bookCount) {
    ofstream outFile("library_data.txt");
    if (!outFile) {
        cout << "Error: Unable to save data to file.\n";
        return;
    }

    outFile << bookCount << endl; // Save the number of books
    for (int i = 0; i < bookCount; i++) {
        outFile << titles[i] << endl;
        outFile << authors[i] << endl;
        outFile << genres[i] << endl;
        outFile << availability[i] << endl;
    }

    outFile.close();
    cout << "Library data saved successfully to 'library_data.txt'.\n";
}

void loadFromFile(string titles[], string authors[], string genres[], bool availability[], int& bookCount, int Max_books) {
    ifstream inFile("library_data.txt");
    if (!inFile) {
        cout << "Error: Unable to load data from file. Starting with empty library.\n";
        bookCount = 0;
        return;
    }

    inFile >> bookCount;
    inFile.ignore(); // Ignore leftover newline after reading bookCount
    for (int i = 0; i < bookCount && i < Max_books; i++) {
        getline(inFile, titles[i]);
        getline(inFile, authors[i]);
        getline(inFile, genres[i]);
        inFile >> availability[i];
        inFile.ignore(); // Ignore leftover newline after reading availability
    }

    inFile.close();
    cout << "Library data loaded successfully from 'library_data.txt'.\n";
}

void addbook(string titles[], string authors[], string genres[], bool availability[], int& bookCount, int Max_books) {
    if (bookCount >= Max_books) {
        cout << "Library is full. Remove some books to add new ones.\n";
    } else {
        cin.ignore(); // Clear leftover newline
        cout << "\nEnter book details:\n";
        cout << "Title: ";
        getline(cin, titles[bookCount]);
        cout << "Author: ";
        getline(cin, authors[bookCount]);
        cout << "Genre: ";
        getline(cin, genres[bookCount]);
        availability[bookCount] = true; // Mark as available
        bookCount++; // Increment the count
        cout << "\nBook added successfully!\n";
    }
}

void removebook(string titles[], string authors[], string genres[], bool availability[], int& bookCount) {
    if (bookCount == 0) {
        cout << "No books in the library to remove.\n";
    } else {
        cin.ignore();
        string titleToRemove;
        cout << "\nEnter the title of the book to remove: ";
        getline(cin, titleToRemove);

        for (int i = 0; i < bookCount; i++) {
            if (titles[i] == titleToRemove) {
                for (int j = i; j < bookCount - 1; j++) {
                    titles[j] = titles[j + 1];
                    authors[j] = authors[j + 1];
                    genres[j] = genres[j + 1];
                    availability[j] = availability[j + 1];
                }
                bookCount--;
                cout << "\nBook '" << titleToRemove << "' removed successfully!\n";
                return;
            }
        }
        cout << "\nBook not found in the library.\n";
    }
}

void toggleAvailability(string titles[], bool availability[], int bookCount) {
    cin.ignore();
    string titleToToggle;
    cout << "\nEnter the title of the book: ";
    getline(cin, titleToToggle);

    for (int i = 0; i < bookCount; i++) {
        if (titles[i] == titleToToggle) {
            if (availability[i]) {
                availability[i] = false;
                cout << "\nBook '" << titles[i] << "' has been borrowed.\n";
            } else {
                availability[i] = true;
                cout << "\nBook '" << titles[i] << "' has been returned.\n";
            }
            return;
        }
    }
    cout << "\nBook not found in the library.\n";
}

void displayBooks(string titles[], string authors[], string genres[], bool availability[], int bookCount) {
    cout << "\n------------ Displaying all books in the library -----------\n";
    cout << left << setw(20) << "Title" << setw(20) << "Author" << setw(20) << "Genre" << "Availability\n";
    cout << "-----------------------------------------------------------\n";

    for (int i = 0; i < bookCount; i++) {
        cout << left << setw(20) << titles[i] << setw(20) << authors[i] << setw(20) << genres[i];
        cout << (availability[i] ? "Available" : "Not Available") << "\n";
    }
    cout << "-----------------------------------------------------------\n";
    cout << "Total Books: " << bookCount << endl << endl;
}

int main() {
    const int Max_books = 100;
    string titles[Max_books];
    string authors[Max_books];
    string genres[Max_books];
    bool availability[Max_books];
    int bookCount = 0;

    // Load data from file at the start
    loadFromFile(titles, authors, genres, availability, bookCount, Max_books);

    int choice;
    do {
        cout << "\nLibrary System\n";
        cout << "1 - Add Book\n"; // aimen
        cout << "2 - Remove Book\n"; // aimen
        cout << "3 - Display Books\n"; // ihsan
        cout << "4 - Borrow/Return Book\n"; // aleena
        cout << "5 - Save to File\n"; // aleena.
        cout << "6 - Load from File\n"; // ihsan.
        cout << "7 - Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) {
            addbook(titles, authors, genres, availability, bookCount, Max_books);
        } else if (choice == 2) {
            removebook(titles, authors, genres, availability, bookCount);
        } else if (choice == 3) {
            displayBooks(titles, authors, genres, availability, bookCount);
        } else if (choice == 4) {
            toggleAvailability(titles, availability, bookCount);
        } else if (choice == 5) {
            saveToFile(titles, authors, genres, availability, bookCount);
        } else if (choice == 6) {
            loadFromFile(titles, authors, genres, availability, bookCount, Max_books);
        }
    } while (choice != 7);

    cout << "\nThank you for using the library system. Goodbye!\n";
}
