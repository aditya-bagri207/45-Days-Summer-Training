class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student = Student("Aditya", 20, "Data Science")

print("Name:", student.name)
print("Age:", student.age)
print("Course:", student.course)