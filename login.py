import csv

username = input("Enter Username: ")
password = input("Enter Password: ")

found = False

with open("../Data/login.csv","r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        if row["Username"] == username and row["Password"] == password:

            print("Login Successful")
            found = True
            break

if not found:
    print("Invalid Username or Password")
