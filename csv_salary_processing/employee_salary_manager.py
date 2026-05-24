import csv
import os
import sys

# Function to calculate total salary
def calculate_salary(basic_pay):
    hra = 0.20 * basic_pay
    da = 0.10 * basic_pay
    total_salary = basic_pay + hra + da
    return total_salary

filename = input("Enter CSV file name: ")

# Check whether file exists
if os.path.isfile(filename):

    file = open(filename, "r")
    reader = csv.reader(file)

    print("\nEmployee Details")
    print("---------------------------")

    # Read each row from CSV file
    for row in reader:

        emp_id = row[0]
        name = row[1]
        basic_pay = float(row[2])

        total_salary = calculate_salary(basic_pay)

        print("Employee ID   :", emp_id)
        print("Employee Name :", name)
        print("Basic Pay     :", basic_pay)
        print("Total Salary  :", total_salary)
        print("---------------------------")

    file.close()

else:
    print("File does not exist")
    sys.exit(0)
