# # problem 1 : Create a program that takes a word from the user and translates it to english
# # words = {
# #     "insan": "human",
# #     "kitap": "book",
# #     "phal": "fruit",
# # }

# # input = input("Enter the word you want to translate to english: ")

# # print(
# #     words.get(input, "Word not found")
# # )  # it wil return the value of key if key is not present it will return the second argument


# # problem 2 : write a program to take 8 numbers and print them only if they are unique

# set = set()

# takeInput = int(input("Enter random number : "))
# set.add(takeInput)

# takeInput1 = int(input("Enter random number : "))
# set.add(takeInput1)

# takeInput2 = int(input("Enter random number : "))
# set.add(takeInput2)

# takeInput3 = int(input("Enter random number : "))
# set.add(takeInput3)

# takeInput4 = int(input("Enter random number : "))
# set.add(takeInput4)

# takeInput5 = int(input("Enter random number : "))
# set.add(takeInput5)

# takeInput6 = int(input("Enter random number : "))
# set.add(takeInput6)

# takeInput7 = int(input("Enter random number : "))
# set.add(takeInput7)

# takeInput8 = int(input("Enter random number : "))
# set.add(takeInput8)

# print(set)

# set = {
#     18,
#     "18",
# }  # checking if 18 will be printed if they same but in different data type

# print(set)

# problem 3 : write an empty dictionary, allow 4 friends to enter there favourite language as value and use there name as key, assume that the names are unique

languages = {}

name = input("Enter your name : ")
takeLanguage = input("Enter your favourite language : ")
languages[name] = takeLanguage

name1 = input("Enter your name : ")
takeLanguage1 = input("Enter your favourite language : ")
languages[name1] = takeLanguage1

name2 = input("Enter your name : ")
takeLanguage2 = input("Enter your favourite language : ")
languages[name2] = takeLanguage2

name3 = input("Enter your name : ")
takeLanguage3 = input("Enter your favourite language : ")
languages[name3] = takeLanguage3

print(languages)
