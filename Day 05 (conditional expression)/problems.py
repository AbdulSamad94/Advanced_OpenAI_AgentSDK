# problem 1 : write a program to find the greatest number among 4 numbers entered by user

takeInput1 = int(input("Enter your first number: "))
takeInput2 = int(input("Enter your second number: "))
takeInput3 = int(input("Enter your third number: "))
takeInput4 = int(input("Enter your fourth number: "))

if takeInput1 > takeInput2 and takeInput1 > takeInput3 and takeInput1 > takeInput4:
    print("The Greatest Number is : ", takeInput1)
elif takeInput2 > takeInput1 and takeInput2 > takeInput3 and takeInput2 > takeInput4:
    print("The Greatest Number is : ", takeInput2)
elif takeInput3 > takeInput1 and takeInput3 > takeInput2 and takeInput3 > takeInput4:
    print("The Greatest Number is : ", takeInput3)
elif takeInput4 > takeInput1 and takeInput4 > takeInput2 and takeInput4 > takeInput3:
    print("The Greatest Number is : ", takeInput4)
else:
    print("All numbers are equal")

# problem 2, write a program that takes input of marks of 3 subject the passing percentage is 40% and subject passing percentage is 33%


marksInput = int(input("Enter Yout 1st Subject Marks: "))
marksInput2 = int(input("Enter Yout 2nt Subject Marks: "))
marksInput3 = int(input("Enter Yout 3rd Subject Marks: "))

if marksInput > 100 or marksInput2 > 100 or marksInput3 > 100:
    print("Invalid marks enter the marks below 100")

totalPercentage = (marksInput + marksInput2 + marksInput2) / 300 * 100

if (
    totalPercentage >= 40
    and marksInput >= 33
    and marksInput2 >= 33
    and marksInput3 >= 33
):
    print("Congratulations you are passed")

else:
    print("Unfortunately you are not passed")


takeInput = input("enter your name: ")

if "abdul" in takeInput:
    print("Your name must be one of allah names")
elif "muhammed" in takeInput:
    print("your name is one of muhammed's name")

# so the in keyword checks if the string is in the string and if it is it returns true otherwise it returns false
# so we can use this keyword to check if the string is in the string and if it is it returns true otherwise it returns false

# problem 3 : write a program to check if the user's username is valid

username = input("Enter your username: ")

if len(username) > 10 and len(username) < 30:
    print("Your username is valid")

else:
    print("Invalid userName")

# problem 4 : write a program that finds a word that is in the list or not

list = ["Abdul", "Samad", "Ali", "Hamzah", "Uzair", "Abdullah"]
word = input("Enter the word you want to search: ")

if word in list:
    print("The word is in the list")

else:
    print("The word is not in the list")
