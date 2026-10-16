# Q12: Maximum and minimum marks

students = {
    "Rahul": 85,
    "Priya": 92,
    "Aman": 78,
    "Neha": 88
}

maximum = None
minimum = None

for marks in students.values():
    if maximum is None or marks > maximum:
        maximum = marks

    if minimum is None or marks < minimum:
        minimum = marks

print("Maximum marks:", maximum)
print("Minimum marks:", minimum)