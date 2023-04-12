"""Function to prompt user input"""
def get_employee_details(first_name, last_name, age, dob, emp_date, department, salary):
    first_name = input("Enter Employee First Name: ")
    last_name = input("Enter Employee Last Name:")
    age = int(input("Enter Employee Age: "))
    emp_date = input("Enter Employee Date of Employment (YYYY-MM-DD): ")
    department = input("Enter Employee Department: ")
    salary = input("Enter Employee Salary: ")

