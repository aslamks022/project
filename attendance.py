# Attendance Management System

import csv

print("==== ATTENDANCE MANAGEMENT SYSTEM ====")

# Function to display menu
def menu():
    print("\n1. Mark Attendance")
    print("2. Calculate Attendance")
    print("3. Display Student Details")
    print("4. Exit")


# Function to mark attendance
def mark_attendance():
    name = input("Enter Student Name: ")
    status = input("Enter Attendance (Present/Absent): ")

    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, status])

    print("Attendance Marked Successfully.")


# Function to calculate attendance percentage
def calculate_attendance():
    total = int(input("Enter Total Classes: "))
    present = int(input("Enter Classes Attended: "))

    if total == 0:
        print("Total classes cannot be zero.")
    else:
        percentage = (present / total) * 100
        print("Attendance Percentage:", round(percentage, 2), "%")


# Function to display student details
def display_student():
    try:
        with open("attendance.csv", "r") as file:
            reader = csv.reader(file)

            print("\n----- Student Attendance Records -----")
            for row in reader:
                if len(row) >= 2:
                    print("Name:", row[0], "| Status:", row[1])

    except FileNotFoundError:
        print("No attendance records found.")


# Main Program
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        mark_attendance()

    elif choice == "2":
        calculate_attendance()

    elif choice == "3":
        display_student()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")

    print("-------------------------------")
    print("Attendance Module Ready")
