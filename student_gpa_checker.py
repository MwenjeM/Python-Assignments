# Author: Martha Mwenje
# File Name: student_gpa_checker.py
# Description:
# This program collects student names and GPAs, checks eligibility for the Dean's List 
# or Honor Roll, and displays results until "ZZZ" is entered as the last name.


# Constants
DEANS_LIST: float = 3.5
HONOR_ROLL: float = 3.25
SENTINEL: str = "ZZZ"

# Variables
gpa: float = 0.0
first_name: str = ""
last_name: str = ""

# Main loop
while last_name != SENTINEL:
    # Get the student's last name
    last_name = input("Enter last name (ZZZ to quit): ")
    if last_name == SENTINEL:
        break

    # Get the student's first name
    first_name = input("Enter first name: ")

    # Get the student's GPA
    try:
        gpa = float(input("Enter student GPA: "))
    except ValueError:
        print("Invalid GPA entered. Please enter a numeric value.")
        continue

    # Determine and display qualification
    if gpa >= DEANS_LIST:
        print(f"{first_name} {last_name} has made the Dean's List!")
    elif gpa >= HONOR_ROLL:
        print(f"{first_name} {last_name} has made the Honor Roll!")
    else:
        print(f"{first_name} {last_name} does not qualify for the Dean's List or the Honor Roll.")

print("Program exited!")