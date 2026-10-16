# Q18: Remove a key

data = {"Name": "Rahul", "Age": 20, "Marks": 80}

key = input("Enter key to remove: ")

if key in data:
    del data[key]
    print("Updated dictionary:", data)
else:
    print("Key not found.")