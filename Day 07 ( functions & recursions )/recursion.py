# Recursion in python

# suppose we want to find the factorial of n number using functions


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


takeInput = int(input("Enter your number: "))
print(factorial(takeInput))

# so in this code, we are calling the factorial function recursively means we are calling the factorial function inside itself. The recursion stops when we reach the base case where n is either 0 or 1, at which point we return 1. The factorial of a number is the product of all positive integers less than or equal to that number. For example, the factorial of 5 is 5 * 4 * 3 * 2 *, in easy words the function which call itself is called recursive function. The factorial of 0 is 1 because there are no numbers less than or equal to 0. The factorial of 1 is 1 because there is only one number less than or equal to 1, which is 0. The factorial of 2 is 2 because there are two numbers less than or equal to 2 and you have to use if-else condition or the recursion will not work
