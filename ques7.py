# Q7: Check whether list is sorted

numbers = list(map(int, input("Enter list elements: ").split()))

sorted_list = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        sorted_list = False
        break

if sorted_list:
    print("The list is sorted.")
else:
    print("The list is not sorted.")