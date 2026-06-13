class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

s = Student("Aditya", 20, 101)

print("Name:", s.name)
print("Age:", s.age)
print("Roll No:", s.roll_number)