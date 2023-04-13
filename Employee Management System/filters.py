import json
import exceptions as exc
import employee as emp

def initialize():
    try:
        with open('Employee Management System/employees.json', 'rt') as file:
            data = json.load(file)
    except:
        raise exc.FileNotFound()

    return data

def filterByName():
    data = initialize()
    nameString = input("\nEnter name you wish to filter for: ").lower()
    for key, value in data.items():
        if (key != "0" and ((nameString in value["First Name"].lower()) or (nameString in value["Last Name"].lower()))):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()

def filterByAge():
    data = initialize()
    ageString = input("\nEnter age you wish to filter for: ").lower()
    pass










def filterByBirth():
    data = initialize()
    birthString = input("\nEnter year of birth you wish to filter for: ").lower()
    for key, value in data.items():
        if (key != "0" and (birthString in value["Birth"][-4:])):
            print(value)
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()











def filterByEmploymentDate():
    data = initialize()
    empDateString = input("\nEnter year of employment you wish to filter for: ").lower()
    pass










def filterByDepartment():
    data = initialize()
    depString = input("\nEnter department you wish to filter for: ").lower()
    pass









def filterBySalary():
    data = initialize()
    minSalString = input("\nEnter minimum salary you wish to filter for: ").lower()
    maxSalString = input("\nEnter maximum salary you wish to filter for: ").lower()
    pass