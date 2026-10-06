numbers = [12, 45, 7, 89, 23, 156]

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)