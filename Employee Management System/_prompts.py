def get_first_name():
    while True:
        try:
            first_name = input("Enter Employee First Name: ")
            if all(x.isalpha() for x in first_name) and len(first_name) >= 3:
                return first_name
            else:
                print("Error: Invalid input")
        except Exception:
            print("Error: Invalid input")


def get_last_name():
    while True:
        try:
            last_name = input("Enter Employee Last Name: ")
            if all(x.isalpha() for x in last_name) and len(last_name) >= 3:
                return last_name
            else:
                print("Error: Invalid input")
        except Exception:
            print("Error: Invalid input")


def get_age():
    while True:
        try:
            return int(input("Enter Employee Age: "))
        except Exception:
            print("Error: Invalid input")


def get_dob():
    while True:
        try:
            dob = input("Enter Employee Date of Birth (DD-MM-YYYY): ")
            if len(dob) == 10 and dob[2] == "-" and dob[5] == "-" and dob[:2].isdigit() and dob[3:5].isdigit() and dob[6:].isdigit():
                return dob
            else:
                print("Error: Invalid input")
        except Exception:
            print("Error: Invalid input")


def get_emp_date():
    while True:
        try:
            emp_date = input(
                "Enter Employee Date of Employment (DD-MM-YYYY): ")
            if len(emp_date) == 10 and emp_date[2] == "-" and emp_date[5] == "-" and emp_date[:2].isdigit() and emp_date[3:5].isdigit() and emp_date[6:].isdigit():
                return emp_date
            else:
                print("Error: Invalid input")
        except Exception:
            print("Error: Invalid input")


def get_department():
    while True:
        try:
            department = input("Enter Employee Department: ")
            if all(x.isalpha() or x.isspace() for x in department) and len(department) >= 3:
                return department
            else:
                print("Error: Invalid input")
        except Exception:
            print("Error: Invalid input")


def get_salary():
    while True:
        try:
            return input("Enter Employee Salary: ")
        except Exception:
            print("Error: Invalid input")


"""def get_employee_details():
    first_name = get_first_name()
    last_name = get_last_name()
    age = get_age()
    dob = get_dob()
    emp_date = get_emp_date()
    department = get_department()
    salary = get_salary()
    return (first_name, last_name, age, dob, emp_date, department, salary)"""
