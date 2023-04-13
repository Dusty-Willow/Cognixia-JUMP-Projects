class EmployeeNotFound():
    
    def __init__(self) -> None:
        print("\nThis employee does not exist.")

class FileNotFound(Exception):
    
    def __init__(self) -> None:
        print("\nThe file employees.json does not exist.")