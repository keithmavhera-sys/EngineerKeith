while True:
    password = input("Enter your password: ")

    if len(password) < 3:
        print("Password is too short!")
    else:
        print("Password stored!")
        break


count = 0

while True:
    passw = input("Enter your Login Password: ")

    if passw == password:
        print("Access granted!")
        break

    else:
        print(f"Wrong password! {2 - count} attempts left!!")
        count += 1

        if count > 2:
            print("Access denied!")
            break

