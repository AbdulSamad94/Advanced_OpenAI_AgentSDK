# problem 1, find the greatest number
# def greatestNumber(a, b, c):
#     if a > b and a > c:
#         print("The greatest number is: ", a)
#     elif b > c and b > a:
#         print("The greatest number is: ", b)
#     elif c > a and c > b:
#         print("The greatest number is: ", c)
#     else:
#         print("numbers are equal")


# numberOne = int(input("Enter your first number: "))
# numberTwo = int(input("Enter your first number: "))
# numberThree = int(input("Enter your first number: "))

# greatestNumber(numberOne, numberTwo, numberThree)

# problem 2, conver the fahrenheit to celsius


# def celsiusToFahrenheit(params):
#     return 5 * (params - 32) / 9


# a = int(input("Enter your temperature in celsius: "))
# call = celsiusToFahrenheit(a)
# print(f" The Temperature is {round(call, 2)}°C")

# problem 3, make a progarm that takes a number and prints the sum of all numbers from natural number to the given number


# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n - 1)


# takeInput = int(input("Enter your number: "))
# call = sum(takeInput)
# print(call)


# problem 4, write a program to make the pattern using recursion


# def patter(e):
#     if e == 0:
#         return 0
#     print("*" * e)
#     patter(e - 1)

# patter(3)

list = ["Abdul Samad", "Hamzah", "Ali", "Ahmed"]
takeInput = input("Enter the name: ")


def removeAndSpit(list, word):
    stripedList = []
    for i in list:
        if i == word:
            list.remove(word)
            stripedList.append(word)
            return stripedList
    else:
        print("name not found")


a = removeAndSpit(list, takeInput)
print(f"The Striped list is: {a} ")
print(f"The updated List is: {list}")
