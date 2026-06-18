class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "D"

s1 = Student("Aditya", 92)
s2 = Student("Rahul", 70)

print(s1.name, "-", s1.grade())
print(s2.name, "-", s2.grade())