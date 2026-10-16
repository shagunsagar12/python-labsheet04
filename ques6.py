# Q6: Split list into two halves

numbers = list(map(int, input("Enter list elements: ").split()))

mid = len(numbers) // 2

first_half = numbers[:mid]
second_half = numbers[mid:]

print("First half:", first_half)
print("Second half:", second_half)