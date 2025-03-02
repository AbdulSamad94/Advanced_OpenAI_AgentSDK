# # # problem 1, take input from the user and store it in list

fruit = []
inputs = input("Enter fruit name: ")
fruit.append(inputs)
print("Your List of fruits are currently this : \n", fruit)

input2 = input("Enter fruit name: ")
fruit.append(input2)
print("Your List of fruits are currently this : \n", fruit)

input3 = input("Enter fruit name: ")
fruit.append(input3)
print("Your List of fruits are currently this : \n", fruit)

input4 = input("Enter fruit name: ")
fruit.append(input4)
print("Your List of fruits are currently this : \n", fruit)


# # # Problem 2, take input from the user of 6 student marks and store them in sorted list

marks = []

takeInput = int(input("Enter marks of student: "))
marks.append(takeInput)

takeInput2 = int(input("Enter marks of student: "))
marks.append(takeInput2)

takeInput3 = int(input("Enter marks of student: "))
marks.append(takeInput3)

takeInput4 = int(input("Enter marks of student: "))
marks.append(takeInput4)

takeInput5 = int(input("Enter marks of student: "))
marks.append(takeInput5)

takeInput6 = int(input("Enter marks of student: "))
marks.append(takeInput6)

marks.sort()
print("Your sorted list of marks is: \n", marks)


# # problem 3, check the changing of element in list and tuple

list = ["Furit", "Dream", 34, 90]
list[0] = "Apple"
print(list)  # List will change

tuple = ("Furit", "Dream", 34, 90)
tuple[0] = "Apple"
print(tuple)  # Tuple will not change


# # problem 4, write a program take sum the list of 4 numbers

list = []

takeInput = int(input("Enter number: "))
list.append(takeInput)
takeInput2 = int(input("Enter number: "))
list.append(takeInput2)
takeInput3 = int(input("Enter number: "))
list.append(takeInput3)
takeInput4 = int(input("Enter number: "))
list.append(takeInput4)


totalSum = sum(
    list
)  # how the fug its a builtin function in python to sum the arrayyy/list
print("Your Total is : ", totalSum)


# problem 5, write a program to count a total number of elements in a tuple

tuple = (6, 7, 7, 5, 2, 2, 4, 5, 6)

countedTuple = tuple.count(7)

print(countedTuple)
