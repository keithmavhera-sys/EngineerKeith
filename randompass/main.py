import random
import string

choice = input("Hello! Do you want to Create or Generate Password? C/G? ").upper()

# CREATE PASSWORD
if choice == "C":

    while True:
        password = input("Enter your password: ")

        if len(password) < 3:
            print("Password is too short!")

        else:
            print("Password stored!")
            break


# GENERATE PASSWORD
elif choice == "G":

    while True:
        length = int(input("How long should the password be? "))

        if length < 3:
            print("Password must be at least 3 characters!")

        else:
            characters = string.ascii_letters + string.digits + "!@#$%^&*"

            password = ""

            for i in range(length):
                password += random.choice(characters)

            print("Generated password:", password)
            break


# INVALID CHOICE
else:
    print("Invalid choice!")
    exit()


# LOGIN
count = 0

while True:
    passw = input("Enter your Login Password: ")

    if passw == password:
        print("Access granted!")
        break

    else:
        count += 1
        print(f"Wrong password! {3 - count} attempts left!")

        if count == 3:
            print("Access denied!")
            break