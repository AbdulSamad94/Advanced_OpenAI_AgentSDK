import random


def game():
    random_Number = random.randint(1, 100)
    total_Guesses = 1

    print("\nWelcome to the Number Guessing Game!\n")

    while True:
        try:
            userInput = int(input("Guess a number between 1 and 10: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while userInput != random_Number:
        if userInput < random_Number:
            print("Guess higher!\n")
        else:
            print("Guess lower!\n")

        while True:
            try:
                userInput = int(input("Guess again: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        total_Guesses += 1
    print("You guessed it! The number was:", random_Number)
    print("Your total guesses were:", total_Guesses)


game()
