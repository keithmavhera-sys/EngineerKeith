Numbers = []

for i in range(5):
    number = int(input("Enter number: "))
    Numbers.append(number)

print("\nNumbers:", Numbers)

# Find total
total = 0

for number in Numbers:
    total += number

# Find largest
largest = Numbers[0]

for number in Numbers:
    if number > largest:
        largest = number

# Find smallest
smallest = Numbers[0]

for number in Numbers:
    if number < smallest:
        smallest = number

# Calculate average
average = total / len(Numbers)

print("Largest:", largest)
print("Smallest:", smallest)
print("Total:", total)
print("Average:", average)