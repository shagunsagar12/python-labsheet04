# Q3: Remove negative numbers

numbers = list(map(int, input("Enter list elements: ").split()))

positive_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)

print("List after removing negative numbers:", positive_numbers)