import manager
import exceptions as exceptions
import json

system_lib = {
    1: "Display",
    2: "Add",
    3: "Update",
    4: "Remove",
    5: "Filter",
    6: "Exit"
}

try:
    with open('employees.json', 'rt') as file:
        data = json.load(file)
except:
    raise exceptions.FileNotFound()

while True:
    print(f"-----------------------------\nSystem Commands:\n1: {system_lib[1]}\n2: {system_lib[2]}\n3: {system_lib[3]}\n4: {system_lib[4]}\n5: {system_lib[5]}\n6: Exit\n")
    ID_type = input("\nWhat would you like to Access? Input system command: ").title()

    if (ID_type == system_lib[1] or ID_type == "1"):
       #Displaying list of current employees
        manager.displayEmployeeList()
        ID_type = None

    elif (ID_type == system_lib[2] or ID_type == "2"):
        #Adding employees
        manager.addEmployee()
        ID_type = None

    elif (ID_type == system_lib[3] or ID_type == "3"):
        # Update method
        manager.updateEmployeeData()
        ID_type = None

    elif (ID_type == system_lib[4] or ID_type == "4"):
        #Remove method
        manager.removeEmployee()
        ID_type = None

    elif (ID_type == system_lib[5] or ID_type == "5"):
        # Filter method
        manager.filterEmployee()
        ID_type = None

    elif (ID_type == system_lib[6] or ID_type == "6"):
        break

    else:
        print("Invalid Command.")   