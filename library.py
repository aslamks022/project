# Library Management System

import csv

print("==== LIBRARY MANAGEMENT SYSTEM ====")


# Function to display menu
def menu():
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")


# Function to add a book
def add_book():
    book = input("Enter Book Name: ")

    if book == "":
        print("Book Name cannot be empty.")
        return

    with open("books.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book])

    print("Book Added Successfully.")


# Function to search for a book
def search_book():
    book = input("Enter Book Name to Search: ")

    if book == "":
        print("Book Name cannot be empty.")
        return

    found = False

    try:
        with open("books.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row and book.lower() == row[0].lower():
                    found = True
                    break

        if found:
            print("Book Found.")
        else:
            print("Book Not Found.")

    except FileNotFoundError:
        print("No books available in the library.")


# Function to issue a book
def issue_book():
    book = input("Enter Book Name to Issue: ")

    if book == "":
        print("Book Name cannot be empty.")
        return

    print("Processing Book Issue...")
    print("Book Issued Successfully.")


# Function to return a book
def return_book():
    book = input("Enter Book Name to Return: ")

    if book == "":
        print("Book Name cannot be empty.")
        return

    print("Processing Book Return...")
    print("Book Returned Successfully.")


# Main Program
while True:
    menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        search_book()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("Exiting Library System...")
        print("Thank you for using the Library Management System.")
        print("--------------------------------------")
        print("Library Module Ready")
        break

    else:
        print("Invalid Choice.")
