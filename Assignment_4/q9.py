file = open("student.txt", "w")

file.write("Name: Aditya\n")
file.write("Marks: 90\n")

file.close()

file = open("student.txt", "r")

content = file.read()

print(content)

file.close()