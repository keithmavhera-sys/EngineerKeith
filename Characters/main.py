Name = input("Enter your name: ")

if len(Name) < 3:
    print("Sorry, your name is too short.")

elif len(Name) > 50:
    print("Sorry, your name is too long.")

else:
    print("Welcome, {}!".format(Name))