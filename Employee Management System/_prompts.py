"""This module contains reusable code for prompting user to input employee details.
        Functions: get_employee_details():
        Prompts the user to input employee details including first name, last name, DOB, age,
        date of employment, salary, and department. Returns a tuple containing all the details.
        """


def get_employee_details():
        """Function to collect employee info """
        first_name = input("Enter Employee First Name: ")
        last_name = input("Enter Employee Last Name: ")
        dob = input("Enter Employee Date of Birth (YYYY-MM-DD): ")
        age = int(input("Enter Employee Age: "))
        emp_date = input("Enter Employee Date of Employment (YYYY-MM-DD): ")
        salary = int(input("Enter Employee Salary: "))
        department = input("Enter Employee Department: ")

        return first_name, last_name, dob, age, emp_date, salary, department
