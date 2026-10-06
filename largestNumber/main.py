numbers = [1, 2, 3, 4, 5, 16, 7, 8, 9, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)