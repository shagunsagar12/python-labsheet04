# Q4: Find product of all elements

numbers = list(map(int, input("Enter list elements: ").split()))

product = 1

for num in numbers:
    product *= num

print("Product =", product)