import random

randomNumber = random.randint(1, 3)

computer = "".lower()
user = input("Enter your choice: Snake, Water, Gun: ").lower()
emoji = ""
computerEmoji = ""

if randomNumber == 1:
    computer = "snake"
    computerEmoji = "🐍"
elif randomNumber == 2:
    computer = "water"
    computerEmoji = "💧"
else:
    computer = "gun"
    computerEmoji = "🔫"

if user == "snake":
    emoji = "🐍"

elif user == "water":
    emoji = "💧"
else:
    emoji = "🔫"


def game():
    if not (user == "gun" or user == "snake" or user == "water"):
        print("Enter a valid choice")
        exit()

    if user == computer:
        print(f" It's a tie, {emoji}  vs {computerEmoji}")
    elif (
        (user == "snake" and computer == "water")
        or (user == "water" and computer == "gun")
        or (user == "gun" and computer == "snake")
    ):
        print(f" You win, {emoji}  vs {computerEmoji}")
    else:
        print(f" You lose, {emoji}  vs {computerEmoji}")


game()
