# problem 1, write a progarm to print a table of the number given by the user


takeInput = int(input("Enter your number: "))

for i in range(1, 11):
    print(f"{takeInput} x {i} = {takeInput * i}")


# problem 2, write a program that will greet the people in the list only the name that will start from S


list = ["Samad", "Abdul", "Hamzah", "Ali", "Ahmed", "Siddiqui", "Sarah"]

for i in list:
    if i.startswith("S") or i.startswith("s"):
        print("Special hi to ", i)
    else:
        print("Hi to ", i)


# problem 3, do the problem 1 with while loop


takeinput = int(input("Enter your number: "))

i = 1

while i < 11:
    print(f"{takeinput} x {i} = {takeinput * i}")
    i += 1


# problem 4, write a program to check if the given number is prime or not


takeinput = int(input("Enter your number: "))

for i in range(2, takeinput):
    if takeinput % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")


# problem 5, write a program to make the sum of all numbers from natural number to the given number


takeInput = int(input("Enter your number: "))

i = 0
sum = 0
while i <= takeInput:
    sum = i + sum
    print(sum)
    i += 1


# problem 6, write a program to print the factorial of a number


takeInput = int(input("Enter your number: "))

sum = 1

for i in range(1, takeInput + 1):
    sum = i * sum

print(sum)


# problem 7, write a program to print the pattern of stars

"""

  *
 ***
*****

"""

n = int(input("Enter your number: "))
for i in range(1, (n + 1)):
    print(" " * (n - i) + "*" * (2 * i - 1))


# problem 8, write a program to print the pattern of stars

"""

*
**
***

"""


n = int(input("Enter your number: "))

for i in range(1, (n + 1)):
    print("*" * (i))


# problem 9, write a program to print the following pattern

"""

***
* *
***

"""


# n = int(input("Enter your number: "))
n: int = input("Enter your number")

for i in range(1, n + 1):
    if i != 1 and i != n:
        print("*" + " " * (n - 2) + "*")
    else:
        print("*" * n)


# problem 10, write a program that will make the multiplication table of the number given by the user in reverse


takeInput = int(input("Enter your number: "))

for i in range(1, 11):
    print(f"{takeInput} x {11 - i} = {takeInput * (11 - i)}")
