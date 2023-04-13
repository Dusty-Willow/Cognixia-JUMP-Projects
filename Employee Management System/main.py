import employee
import manager
system_lib = {
    1: "Display",
    2: "Add",
    3: "Update"
}

while True:
    print(f"-----------------------------\nSystem Library:\n1:  {system_lib[1]}\n2: {system_lib[2]}\n3: {system_lib[3]}\n")
    ID_type = input("\nWhat would you like to Access? Input system ID, or type 'exit' to exit:\t").capitalize()

    if ID_type == '1':
       #Displaying list of current employees
        manager.displayEmployeeList()
        ID_type = None

    elif ID_type == '2':
        #Adding employees
        employee()
        ID_type = None

    elif ID_type == '3':
        # Update method
        manager.updateEmployeeData()

    elif ID_type == 'Exit':
        break   