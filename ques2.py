# Q2: Rotate a list by n positions

numbers = list(map(int, input("Enter list elements: ").split()))
n = int(input("Enter number of positions: "))

n = n % len(numbers)

rotated = numbers[-n:] + numbers[:-n]

print("Rotated list:", rotated)