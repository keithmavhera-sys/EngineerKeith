Car_Started = False

while True:
    command = input("> ")

    if command.upper() == "START":
        if Car_Started:
            print("Car is started already.")
        else:
            print("Car has started.")
            Car_Started = True

    elif command.upper() == "STOP":
        if not Car_Started:
            print("Car is stopped already.")
        else:
            print("Car has stopped.")
            Car_Started = False

    elif command.upper() == "HELP":
        print("""
Start - to start the car
Stop - to stop the car
Exit - to exit the car
""")

    elif command.upper() == "EXIT":
        break

    else:
        print("I don't know how to handle this command.")