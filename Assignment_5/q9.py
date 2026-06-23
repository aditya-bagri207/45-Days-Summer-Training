import matplotlib.pyplot as plt

# Line Plot

subjects = ["Math", "Science", "English", "Computer", "Physics"]
marks = [85, 90, 78, 95, 88]

plt.plot(subjects, marks, marker="o", label="Marks")

plt.title("Marks Trend Across 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)

plt.show()


# Bar Chart

students = ["Aditya", "Rahul", "Aman", "Riya", "Kriti"]
student_marks = [85, 72, 91, 78, 88]

plt.bar(students, student_marks, label="Marks")

plt.title("Marks of 5 Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)

plt.show()