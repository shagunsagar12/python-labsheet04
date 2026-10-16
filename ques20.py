# Q20: Sum of dictionary values

data = {
    "Math": 80,
    "English": 75,
    "Python": 90
}

total = 0

for value in data.values():
    total += value

print("Sum of values:", total)