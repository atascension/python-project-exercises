import random

user_guess_bracket = []
attempts = 0
game_number = random.randint(1, 10)

print("")
print("""Welcome to the number guessing game!
You will have 5 attempts to guess the correct number.
---------------------------
""")

while attempts < 5:
    user_guess = int(input("Choose a number between 1 and 10: "))

    if user_guess < 1 or user_guess > 10:
        print("Sorry, that number is outside of the requested range. Please choose a number between 1 and 10.")
        continue
    elif user_guess < game_number:
        user_guess_bracket.append(user_guess)
        attempts += 1
        if attempts == 5:
            print()
            print(f"Sorry, you ran out of attempts. The correct number is: {game_number} ")
            print("Here are your previous attempts: ", end="")
            for guess in user_guess_bracket:
                print(guess, end= ", ")
            print()
            break
        else:
            print("Sorry that guess is too low, try again!")
    elif user_guess > game_number:
        user_guess_bracket.append(user_guess)
        attempts += 1
        if attempts == 5:
            print()
            print(f"Sorry, you ran out of attempts. The correct number is: {game_number} ")
            print("Here are your previous attempts: ", end="")
            for guess in user_guess_bracket:
                print(guess, end= ", ")
            print()
        else:
            print("Sorry that guess is too high, try again!")
    else:
        print()
        print("Congratulations, you guessed the correct number!")
        print("Here are your previous attempts: ", end="")
        for guess in user_guess_bracket:
            print(guess, end= ", ")
        print()
        break

        
       




