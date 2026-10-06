i = 0
guess = 8
while i <= 2:
    num = int(input("Guess a number: "))
    i += 1
    if num != guess:
        print(f"You guessed {num}. Try again")
        if i == 3:
            print("You exhausted")
            break

    else:
        print(f"You guessed {num}. Well done")
        break

