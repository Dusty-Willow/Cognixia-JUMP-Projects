import json
import employee as emp
import _prompts as pr
import exceptions as exc


# Methods used for fetching and then displaying list of employees from employees.json
def displayEmployeeList():
    # Loads employee details from relevant file
    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)
    except:
        exc.FileNotFound()

        for key, value in data.items():
            if (key != "0"):
                print(f"-----Employee Number {key}-----\n")
                currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
                currentEmployee.toString()


def addEmployee():   #module adding a new employee record to the json file
    first_name = pr.get_first_name()
    last_name = pr.get_last_name()
    age = pr.get_age()
    dob = pr.get_dob()
    emp_id = generateId()
    emp_date = pr.get_emp_date()
    department = pr.get_department()
    salary = pr.get_salary()
    email = generateEmail(first_name, last_name, dob, emp_id)
    emp_info = {
        "First Name": first_name.title(),
        "Last Name": last_name.title(),
        "Age": age,
        "Birth": dob,
        "Employee ID": emp_id,
        "Employment Date": emp_date,
        "Department": department.title(),
        "Salary": salary,
        "Email": email
                }
    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)
    except:
        exc.FileNotFound()

    data[emp_id] = emp_info
    
    try:
        with open('employees.json', 'w') as file:
            json.dump(data, file, indent=4)
    except:
        exc.FileNotFound()

def generateEmail(first_name, last_name, dob, emp_id):
    email = f"{first_name}.{last_name}{dob[-2:]}{emp_id}@cognixia.com"
    return email

def generateId():
    employeeIdPlaceholder = None

    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)
    except:
        exc.FileNotFound()

    employeeIdPlaceholder = data["0"]
    data["0"] = employeeIdPlaceholder + 1

    try:
        with open('employees.json', 'w') as file:
            json.dump(data, file, indent=4)
    except:
        exc.FileNotFound()

    return employeeIdPlaceholder + 1

# Method used for updating Employee data in employees.json
def updateEmployeeAttribute(emp_id, attribute, value):
    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)
    except:
        exc.FileNotFound()

        data[str(emp_id)][attribute] =  value

    try:
        with open('employees.json', 'w') as file:
            json.dump(data, file, indent=4)
    except:
        exc.FileNotFound()

def updateEmail(emp_id):
    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)
    except:
        exc.FileNotFound()

        data[str(emp_id)]["Email"] = generateEmail(data[str(emp_id)]["First Name"], data[str(emp_id)]["Last Name"], data[str(emp_id)]["Birth"], data[str(emp_id)]["Employee ID"])

    try:
        with open('employees.json', 'w') as file:
            json.dump(data, file, indent=4)
    except:
        exc.FileNotFound()

def updateEmployeeData():
    updateEmployee = True
    employeePos = None
    employeeID = input("Please enter the Employee Id of the Employee you wish to update: ")
    try:
        with open('employees.json', 'rt') as file:
                data = json.load(file)
    except:
        exc.FileNotFound()
    employeeFound = False
    for key, value in data.items():
        if (employeeID == key and employeeID != "0"):
            employeeFound = True

    if (employeeFound == False):
        exc.EmployeeNotFound()
        updateEmployee = False

    while updateEmployee:
        print(f"You may update the following:\n1 First Name \n2 Last Name\n3 Age\n4 Birth\n5 Employment Date\n6 Department\n7 Salary\n")
        updateField = input(f"What would you like to update for this employee? ")
        match updateField.title():
            case "First Name":
                updateEmployeeAttribute(employeeID, "First Name", pr.get_first_name())
                updateEmail(employeeID)
            case "Last Name":
                updateEmployeeAttribute(employeeID, "Last Name", pr.get_last_name())
                updateEmail(employeeID)
            case "Age":
                updateEmployeeAttribute(employeeID, "Age", int(pr.get_age()))
            case "Birth":
                updateEmployeeAttribute(employeeID, "Birth", pr.get_dob())
                updateEmail(employeeID)
            case "Employment Date":
                updateEmployeeAttribute(employeeID, "Employment Date", pr.get_emp_date())
            case "Department":
                updateEmployeeAttribute(employeeID, "Department", pr.get_department())
            case "Salary":
                updateEmployeeAttribute(employeeID, "Salary", pr.get_salary())
            case _:
                print("Invalid employee field choice. Please choose an appropriate field to update.")

        if (input("Would you like to update anything else? Enter Y/N: ").upper() == "N"):
            updateEmployee = False


def removeEmployee():
    emp_id = input("Please enter the Employee ID for the employee you wish to remove.")
    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)

        del data[emp_id]

        with open('employees.json', 'w') as file:
            json.dump(data, file, indent=4)
    except:
        print("This file doesn't exist.")
