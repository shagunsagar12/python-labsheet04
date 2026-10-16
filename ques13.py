# Q13: Character frequency

text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency:")

for char, count in frequency.items():
    print(char, ":", count)