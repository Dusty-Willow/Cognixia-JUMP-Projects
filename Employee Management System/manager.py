import json
import employee as emp

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
        generateId()
        # printDict()
    except:
        print("This file doesn't exist.")
# Methods used for fetching and then displaying list of employees from employees.json

def generateEmail(firstName, lastName, birth, id):
    email = ""

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
removeEmployee()
