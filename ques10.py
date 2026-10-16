# Q10: Convert list into string without join()

items = input("Enter list elements: ").split()

result = ""

for item in items:
    result += item

print("String:", result)