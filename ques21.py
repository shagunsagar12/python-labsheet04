# Q21: Key with maximum value

data = {
    "Math": 80,
    "English": 75,
    "Python": 90
}

max_key = None
max_value = None

for key, value in data.items():
    if max_value is None or value > max_value:
        max_value = value
        max_key = key

print("Key with maximum value:", max_key)
print("Maximum value:", max_value)