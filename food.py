# Food Ordering System

import csv

print("==== FOOD ORDERING SYSTEM ====")

# Function to display food menu
def display_menu():
    print("\n------ MENU ------")
    print("1. Idli  - Rs. 40")
    print("2. Dosa  - Rs. 60")
    print("3. Meals - Rs. 100")
    print("4. Tea   - Rs. 15")


# Function to place an order
def place_order():
    item = input("Enter food item: ")

    if item == "":
        print("Food item cannot be empty.")
        return

    with open("menu.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item])

    print("Order Placed Successfully.")
    print("Processing your order...")
    print("Thank you for ordering.")


# Function to calculate bill
def calculate_bill():
    print("\nSelect Food Item")
    print("1. Idli")
    print("2. Dosa")
    print("3. Meals")
    print("4. Tea")

    choice = input("Enter your choice: ")
    quantity = int(input("Enter Quantity: "))

    if choice == "1":
        price = 40
    elif choice == "2":
        price = 60
    elif choice == "3":
        price = 100
    elif choice == "4":
        price = 15
    else:
        print("Invalid Food Choice.")
        return

    total = quantity * price
    print("Calculating Bill...")
    print("Total Bill: Rs.", total)


# Main Program
while True:
    print("\n1. Display Menu")
    print("2. Place Order")
    print("3. Calculate Bill")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_menu()

    elif choice == "2":
        place_order()

    elif choice == "3":
        calculate_bill()

    elif choice == "4":
        print("Exiting Food Ordering System...")
        print("Thank you for visiting the Campus Cafeteria.")
        print("Food Module Ready")
        break

    else:
        print("Invalid Choice. Please try again.")
