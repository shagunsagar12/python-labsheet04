# Q11: Student names and marks

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("\nStudent Details:")

for name, marks in students.items():
    print(name, ":", marks)