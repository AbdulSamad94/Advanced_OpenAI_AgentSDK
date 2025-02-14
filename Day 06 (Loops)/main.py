# ----------------------WHILE LOOPS-------------------------

index = 0

while index < 10:
    print(index)
    index += 1

# if the condition is true then the code inside the while loop will be executed
# if the condition is false then the while loop will stop executing

# priting all names inside a list using while loop

list = ["Abdul", "Samad", "Hamzah", "Ali", "Ahmed"]
index = 0

while index < len(list):
    print(list[index])
    index += 1

# printing to 1 million

i = 0

while i < 1000:
    print(i)
    i += 1


# --------------FOR LOOPS-------------------------

for i in range(4):
    print(i)

for i in range(0, 10, 2):  # start, stop, step
    print(i)

# ----printing list using for loop

list = ["Abdul", "Samad", "Hamzah", "Ali", "Ahmed"]

for i in list:
    print(i)

# ----printing string using for loop

string = "My name is abdul samad siddiqui and i am a full stack developer"

for i in string:
    print(i)

# ------FOR WITH ELSE

list = ["Abdul", "Samad", "Hamzah", "Ali", "Ahmed"]

for i in list:
    print(i)
else:
    print("Work has been done")

# the else will be executed if the for loop completes without any break statement

# ------FOR WITH BREAK

list = ["Abdul", "Samad", "Hamzah", "Ali", "Ahmed"]

for i in list:
    if i == "Hamzah":
        break
    print(i)


# -----FOR WITH CONTINUE

list = ["Abdul", "Samad", "Hamzah", "Ali", "Ahmed"]

for i in list:
    if i == "Hamzah":
        continue
    print(i)

# the continue will skip the current iteration and move to the next iteration means it will skip the hamzah and move on


# -----Pass statement


for i in range(10):
    pass  # -------------------->  it will skip the loop if we dont add pass in the empty loop it will throw an error

print("hello world")
