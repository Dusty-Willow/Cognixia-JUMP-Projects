import json
import employee as emp
import _prompts as pr
import exceptions as exc

employees = []
objectList = []
employeeIdPlaceholder = None

# Methods used for fetching and then displaying list of employees from employees.json
def collector(dict):
    global employees, employeeIdPlaceholder
    employees = dict.keys()
    for key in employees:
        if (key == "0"):
            employeeIdPlaceholder = dict[key]
        else:
            objectList.append(emp.Employee(dict[key]["First Name"], dict[key]["Last Name"], dict[key]["Age"], dict[key]["Birth"], dict[key]["Employee ID"], dict[key]["Employment Date"], dict[key]["Salary"], dict[key]["Department"], dict[key]["Email"]))

def listEmployees():
    global objectList
    empNum = 1
    print("\n")
    for object in objectList:
        print(f"-----Employee Number {str(empNum)}-----\n")
        object.toString()
        empNum += 1

def displayEmployeeList():
    # Loads employee details from relevant file
    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)

        collector(data)
        listEmployees()

        # printDict()
    except:
        print("This file doesn't exist.")

    listEmployees()
# Methods used for fetching and then displaying list of employees from employees.json

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
        data[emp_id] = emp_info

        with open('employees.json', 'w') as file:
            json.dump(data, file, indent=4)
        # printDict()
    except:
        print("This file doesn't exist.")

def generateEmail(first_name, last_name, dob, emp_id):
    email = f"{first_name}.{last_name}{dob[-2:]}{emp_id}@cognixia.com"
    return email

def generateId():
    global employeeIdPlaceholder

    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)
        employeeIdPlaceholder = data["0"]
        data["0"] = employeeIdPlaceholder + 1

        with open('employees.json', 'w') as file:
            json.dump(data, file, indent=4)
    except:
        print("This file doesn't exist.")

    return employeeIdPlaceholder + 1

# Method used for updating Employee data in employees.json
def updateEmployeeAttribute(emp_id, attribute, value):
    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)

        data[str(emp_id)][attribute] =  value

        with open('employees.json', 'w') as file:
            json.dump(data, file, indent=4)
    except:
        print("This file doesn't exist.")

def updateEmployeeData(objectList, employeeID):
    updateEmployee = True
    employeePos = None
    for employee in objectList:
        try:
            if employee.employeeId == employeeID:
                employeePos = objectList.index(employee)
        except exc.EmployeeNotFound as e:
            e.printError()

    while updateEmployee:
        updateField = input(f"What would you like to update for this employee?")
        match updateField.title():
            case "First Name":
                updateEmployeeAttribute(employeeID, "First Name", input("Enter new First Name: "))
            case "Last Name":
                updateEmployeeAttribute(employeeID, "Last Name", input("Enter new Last Name: "))
            case "Age":
                updateEmployeeAttribute(employeeID, "Age", input("Enter new Age: "))
            case "Birth":
                updateEmployeeAttribute(employeeID, "Birth", input("Enter new Birth Date: "))
            case "Employment Date":
                updateEmployeeAttribute(employeeID, "Employment Date", input("Enter new Employment Date: "))
            case "Department":
                updateEmployeeAttribute(employeeID, "Department", input("Enter new Department: "))
            case "Salary":
                updateEmployeeAttribute(employeeID, "Salary", input("Enter new Salary: "))
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

displayEmployeeList()