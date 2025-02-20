import random

# problem 1, write a progarm that find if a read.txt file contains the word "python" or not

# with open("read.txt", "r") as file:
#     data = file.read()
#     if "python" in data:
#         print("The word 'python' is present in the file.")
#     else:
#         print("The word 'python' is not present in the file.")


# problem 2, cant explain xD

random = random.randint(1, 100)

with open("write.txt", "") as file:
    prevHighScore = file.read()


def game():
    print(f"The Random number is ${random}")

    if random > int(prevHighScore):
        print("You have a new high score!")
        with open("write.txt", "w") as file:
            file.write(str(random))
            print("High score! has been updated")
    else:
        print("You have not beaten the previous high score.")


game()
