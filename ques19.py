# Q19: Check whether key exists

data = {
    "Name": "Rahul",
    "Age": 20,
    "Marks": 85
}

key = input("Enter key to search: ")

if key in data:
    print("Key exists.")
else:
    print("Key does not exist.")