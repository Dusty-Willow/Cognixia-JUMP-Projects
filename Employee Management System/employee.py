class Employee:

    def __init__ (self, fName, lName, age, birth, employeeId, employmentDate, department, salary, email):
        self.firstName = fName
        self.lastName = lName
        self.age = age
        self.birth = birth
        self.employeeId = employeeId
        self.employmentDate = employmentDate
        self.department = department
        self.salary = salary
        self.email = email

    def toString(self):
        print(f"Employee Name: {self.firstName} {self.lastName}")
        print(f"Employee Age: {self.age}")
        print(f"Employee Birth Date: {self.birth}")
        print(f"Employee ID: {self.employeeId}")
        print(f"Employment Date: {self.employmentDate}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print(f"Employee Email: {self.email}")
        print("\n")