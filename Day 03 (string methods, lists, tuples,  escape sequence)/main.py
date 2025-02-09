# name = "abdul samad siddiqui"

# # nameLength = name[0:3] # start from 0 and end at 3 but not include 3
# # character = name[1] # 0 is S, 1 is a, 2 is m, 3 is a, 4 is d, so it will print a

# # nagetive slicing

# # nameLength = name[-5: -1] # start from -3 and end at the end of the string
# # character = name[0 : 5] # or we can also do this for easy access name[0 : -1]

# # the output will be the same as the positive slicing

# # print(character)
# # print(nameLength)

# # print(name[:4]) # it will start from 0 and end at 4 but not include 4
# # print(name[4:]) # it will start from 4 and end at the end of the string
# # print(name[:]) # it will start from 0 and end at the end of the string
# # print(name[::2]) # it will start from 0 and end at the end of the string with a step of 2
# # print(name[::-1]) # it will start from the end of the string and end at 0 with a step of -1
# # print(name[1:4:2]) # it will start from 1 and end at 4 but not include 4 with a step of 2
# # print(name[0:4:2]) # it will start from 0 and end at 4 but not include 4 with a step of 2

# print(name.endswith("s")) # it will return True if the string ends with the given character
# print(name.startswith("S")) # it will return True if the string starts with the given character
# print(name.find("a")) # it will return the index of the first occurrence of the given character
# print(name.count("a")) # it will return the number of occurrences of the given character
# print(name.index("a")) # it will return the index of the first occurrence of the given character
# print(name.rfind("a")) # it will return the index of the last occurrence of the given character
# print(name.rindex("a")) # it will return the index of the last occurrence of the given character
# print(name.isalnum()) # it will return True if the string is alphanumeric
# print(name.isalpha()) # it will return True if the string is alphabetic
# print(name.isdigit()) # it will return True if the string is numeric
# print(name.islower()) # it will return True if the string is lowercase
# print(name.isupper()) # it will return True if the string is uppercase
# print(name.isspace()) # it will return True if the string is whitespace
# print(name.istitle()) # it will return True if the string is titlecase
# print(name.lower()) # it will convert the string to lowercase
# print(name.upper()) # it will convert the string to uppercase
# print(name.title()) # it will convert the string to titlecase
# print(name.capitalize()) # it will convert the first character of the string to uppercase
# print(name.swapcase()) # it will swap the case of all characters in the string means lowercase to uppercase and uppercase to lowercase
# print(name.strip()) # it will remove the leading and trailing whitespace
# print(name.lstrip()) # it will remove the leading whitespace
# print(name.rstrip()) # it will remove the trailing whitespace
# print(name.replace("a", "b")) # it will replace all occurrences of the given character with the given character
# print(name.split()) # it will split the string into a list of substrings based on the given delimiter and give the output in an array
# print(name.rsplit()) # it will split the string into a list of substrings based on the given delimiter and give the output in an array
# print(name.partition("a")) # it will split the string into three parts based on the given delimiter


# Escape Sequence in Python

# quote = "He said, I am a programmer" # it will print the string as it is
# # quote = "He said, \"I am a programmer\"" # it will print the double quote in the string
# # quote = "He said, \n I am a programmer" # it will print the string in the next line
# # quote = "He said, \t I am a programmer" # it will print the string in the next tab
# # quote = "He said, \b I am a programmer" # it will print the string in the previous backspace
# # quote = "He said, \f I am a programmer" # it will print the string in the next form feed

# print(quote)