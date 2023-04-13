def get_first_name():
    while True:
        try:
            first_name = input("Enter Employee First Name: ")
            if all(x.isalpha() for x in first_name) and len(first_name) >= 3:
                return first_name
            else:
                print("Error: Name must only use characters between A-Z and be at least 3 characters.")
        except Exception:
            print("Error: Name must only use characters between A-Z and be at least 3 characters.")


def get_last_name():
    while True:
        try:
            last_name = input("Enter Employee Last Name: ")
            if all(x.isalpha() for x in last_name) and len(last_name) >= 3:
                return last_name
            else:
                print(
                    "Error: Name must only include characters between A-Z and be at least 3 characters long.")
        except Exception:
            print("Error: Name must only include characters between A-Z and be at least 3 characters long.")


def get_age():
    while True:
        try:
            age = int(input("Enter Employee Age: "))
            if age > 0:
                return age
            else:
                print("Error: Age must be greater than 0.")
        except ValueError:
            print("Error: Age must be a number.")


def get_dob():
    while True:
        try:
            dob = input("Enter Employee Date of Birth (DD-MM-YYYY): ")
            if len(dob) == 10 and dob[2] == "-" and dob[5] == "-" and dob[:2].isdigit() and dob[3:5].isdigit() and dob[6:].isdigit():
                return dob
            else:
                print("Error: Date must be digits in DD-MM-YYY format.")
        except Exception:
            print("Error: Date must be digits in DD-MM-YYY format.")


def get_emp_date():
    while True:
        try:
            emp_date = input(
                "Enter Employee Date of Employment (DD-MM-YYYY): ")
            if len(emp_date) == 10 and emp_date[2] == "-" and emp_date[5] == "-" and emp_date[:2].isdigit() and emp_date[3:5].isdigit() and emp_date[6:].isdigit():
                return emp_date
            else:
                print("Error: Date must be digits in DD-MM-YYY format.")
        except Exception:
            print("Error: Date must be digits in DD-MM-YYY format.")


def get_department():
    while True:
        try:
            department = input("Enter Employee Department: ")
            if all(x.isalpha() or x.isspace() for x in department) and len(department) >= 3:
                return department
            else:
                print(
                    "Error: Department name must only include characters between A-Z and be at least 3 characters long.")
        except Exception:
            print("Error: Department name must only include characters between A-Z and be at least 3 characters long.")


def get_salary():
    while True:
        try:
            salary = int(input("Enter Employee Salary: "))
            if salary < 0:
                print("Error: Salary must be a positive number.")
            else:
                return salary
        except ValueError:
            print("Error: Salary must be a number.")

