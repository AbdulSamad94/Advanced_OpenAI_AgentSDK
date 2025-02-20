def function():  # Function Defination
    input1 = int(input("Enter you age 1st person: "))
    print("Your name is ", input1)


function()  # Function Call
function()
function()
function()
function()

# Function Argument


def params(name, className):
    print("My Name is" + name)
    print(className)


params("Abdul Samad", "I am in 11th class")

# Return In Function


def returnFunction():
    a = "Hello world"
    return a


a = returnFunction()
print(a)


def returnFunction2():
    print("Hello world 2")
    return "ok"


a = returnFunction2()
print(a)

# Default Arguments


def defualtArgument(name, className="I am in 11th class"):
    print("My Name is", name)
    print(className)


defualtArgument("Abdul Samad")
defualtArgument("Ali", "I am in 12th class")
