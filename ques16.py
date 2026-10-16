# Q16: Sort dictionary by values

data = {"A": 40, "B": 10, "C": 30, "D": 20}

sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print("Original dictionary:", data)
print("Sorted by values:", sorted_data)