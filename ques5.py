# Q5: List of squares from 1 to n

n = int(input("Enter n: "))

squares = []

for i in range(1, n + 1):
    squares.append(i * i)

print("Squares:", squares)