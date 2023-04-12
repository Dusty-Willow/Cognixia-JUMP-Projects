import json
import employee as emp
import exceptions as exc

employees = []
objectList = []

# Methods used for fetching and then displaying list of employees from employees.json
def collector(dict):
    global employees
    employees = dict.keys()
    for key in employees:
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
                

displayEmployeeList()
updateEmployeeData(objectList, 2)