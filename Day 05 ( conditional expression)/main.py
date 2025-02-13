ageInput = int(input("Enter your age: "))

if ageInput > 18:  # -----------------------> if(ageInput > 18): you can also do this
    print("you are an adult")  # -----------------> its in the if-else

else:
    print("you are a minor")  # -----------------> its in the if-else
print(
    "it will run no matter what"
)  # -------------------------------------> its outside the if-else

# so even if the condition is not true the print that doesnot have gap will be printed
# lets make a program that will also use elif


ageInput = int(input("Enter your age: "))

if ageInput >= 18:
    print("You are an adult you can make your CNIC")

elif ageInput <= 0:
    print("please enter a valid age")

elif ageInput < 12:
    print("You are a child you can't make your CNIC")

elif ageInput >= 12:
    print("You are a teenager you still can not make your CNIC")


print("End of the program")

# that's how you make an if-else chain
