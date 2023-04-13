import employee
import manager
system_lib = {
    1: "Display",
    2: "Add",
    3: "Update",
    4: "Remove"
}

while True:
    print(f"-----------------------------\nSystem Commands:\n1: {system_lib[1]}\n2: {system_lib[2]}\n3: {system_lib[3]}\n4: {system_lib[4]}\n5: Exit\n")
    ID_type = input("\nWhat would you like to Access? Input system ID, or type 'exit' to exit:\t").title()

    if ID_type == system_lib[1]:
       #Displaying list of current employees
        manager.displayEmployeeList()
        ID_type = None

    elif ID_type == system_lib[2]:
        #Adding employees
        manager.addEmployee()
        ID_type = None

    elif ID_type == system_lib[3]:
        # Update method
        manager.updateEmployeeData()
        ID_type = None

    elif ID_type == system_lib[4]:
        #Remove method
        manager.removeEmployee()
        ID_type = None

    elif ID_type == 'Exit':
        break   