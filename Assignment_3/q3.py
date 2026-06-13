class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

emp = Employee(101, "Aditya", 50000)

print("ID:", emp.employee_id)
print("Name:", emp.name)
print("Salary:", emp.salary)