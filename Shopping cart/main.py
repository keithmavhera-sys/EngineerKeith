item = []
price = []

while True:
    item.append(input("Please enter item: "))
    price.append(input("Please enter price: "))
    if input("Do you want to add another item? Y/N: ").upper() == "Y":
        item.append(input("Please enter item: "))
        price.append(input("Please enter price: "))

    elif input("Do you want to add another item? Y/N: ").upper() == "N":
        break

    else:
        print("Please enter Y/N")

Total = 0

for i in range(len(item)):
    total = total + int(item[i])



