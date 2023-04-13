import json
import exceptions as exc
import employee as emp
import _prompts as pr

def initialize():
    try:
        with open('employees.json', 'rt') as file:
            data = json.load(file)
    except:
        raise exc.FileNotFound()

    return data


def filterByName():
    entryFound = False
    data = initialize()
    nameString = pr.filterPrompt("Name")
    for key, value in data.items():
        if (key != "0" and ((nameString in value["First Name"].lower()) or (nameString in value["Last Name"].lower()))):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()
            entryFound = True

    if not entryFound:
        print("\nNo entries matching filter settings found!")

def filterByAge():
    entryFound = False
    data = initialize()
    age = pr.filterPrompt("Age")
    for key, value in data.items():
        if (key != "0" and value["Age"] == int(age)):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()
            entryFound = True

    if not entryFound:
        print("\nNo entries matching filter settings found!")


def filterByBirth():
    entryFound = False
    data = initialize()
    birthString = pr.filterPrompt("Birth")
    for key, value in data.items():
        if (key != "0" and (birthString == value["Birth"][-4:])):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()
            entryFound = True

    if not entryFound:
        print("\nNo entries matching filter settings found!")


def filterByEmploymentDate():
    entryFound = False
    data = initialize()
    empDateString = pr.filterPrompt("Employment Date")
    for key, value in data.items():
        if (key != "0" and ((str(empDateString) in value["Employment Date"]))):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()
            entryFound = True

    if not entryFound:
        print("\nNo entries matching filter settings found!")


def filterByDepartment():
    entryFound = False
    data = initialize()
    departmentString = pr.filterPrompt("Department").lower()
    for key, value in data.items():
        if (key != "0" and departmentString in value["Department"].lower()):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()
            entryFound = True

    if not entryFound:
        print("\nNo entries matching filter settings found!")


def filterBySalary():
    entryFound = False
    data = initialize()
    minSalary = int(pr.filterPrompt("Min Salary"))
    maxSalary = int(pr.filterPrompt("Max Salary"))
    for key, value in data.items():
        if (key != "0" and ((minSalary <= int(value["Salary"])) and (maxSalary >= int(value["Salary"])))):
            print(f"Employee Number {key}: \n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()
            entryFound = True

    if not entryFound:
        print("\nNo entries matching filter settings found!")
