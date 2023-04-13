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
    data = initialize()
    nameString = input("\nEnter name you wish to filter for: ").lower()
    for key, value in data.items():
        if (key != "0" and ((nameString in value["First Name"].lower()) or (nameString in value["Last Name"].lower()))):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()


def filterByAge():
    data = initialize()
    while True:
        age = input("\nEnter age you wish to filter for: ")
        if age.isdigit() and int(age) >= 0:
            age = int(age)
            break
        else:
            print("Please enter a number.")
    for key, value in data.items():
        if (key != "0" and value["Age"] == age):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()










def filterByBirth():
    data = initialize()
    birthString = input("\nEnter year of birth you wish to filter for: ").lower()
    pass









def filterByEmploymentDate():
    data = initialize()
    empDateString = pr.start_year_filter()
    for key, value in data.items():
        if (key != "0" and ((str(empDateString) in value["Employment Date"]))):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()






def filterByDepartment():
    data = initialize()
    departmentString = input(
        "\nEnter department you wish to filter for: ").lower()
    for key, value in data.items():
        if (key != "0" and departmentString in value["Department"].lower()):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()









def filterBySalary():
    data = initialize()
    minSalString = input("\nEnter minimum salary you wish to filter for: ").lower()
    maxSalString = input("\nEnter maximum salary you wish to filter for: ").lower()
    pass

