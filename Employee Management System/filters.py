import json
import exceptions as exc
import employee as emp

def initialize():
    try:
        with open('employees.json', 'rt') as file:
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

def filterBySalary():
    data = initialize()
    minSalary = int(input("\nEnter a  minimum salary  you wish to filter for: "))
    maxSalary = int(input("\nEnter a  maximum salary  you wish to filter for: "))
    for key, value in data.items():
        if (key != "0" and ((minSalary <= int(value["Salary"])) and (maxSalary >= int(value["Salary"])))):
            print(f"Employee Number {key} has a salary of: \n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()

filterBySalary()









def filterByBirth():
    data = initialize()
    birthString = input("\nEnter year of birth you wish to filter for: ").lower()
    pass









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