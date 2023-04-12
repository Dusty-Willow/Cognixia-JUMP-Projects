import json
import employee as emp
import _prompts as pr

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
    email = f"{first_name}.{last_name}{dob[-2:]}{id}@cognixia.com"
    return email

def generateId():
    global employeeIdPlaceholder

    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)

        data["0"] = employeeIdPlaceholder + 1

        with open('employees.json', 'w') as file:
            json.dump(data, file, indent=4)
    except:
        print("This file doesn't exist.")

    return str(employeeIdPlaceholder + 1)

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
