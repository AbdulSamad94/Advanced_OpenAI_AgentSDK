"""
-------------------------  Modes of opening a file in python

r --- for reading a file
w --- for reading a file
a --- for appending a file
+ --- for updating a file
rb -- will open the file to read in binary mode
rt -- will open the file to read in text mode


"""

# # reading files using python

# file = open("read.txt", "r")  # ------------------> "r the mode of the file
# data = file.read()
# print(data)
# file.close()

# # writing files using python

# string = "Hello my name is abdul samad siddiqui and i am a good programmer"
# write = open("write.txt", "w")
# write.write(string)
# write.close

# # readlines using python

# file = open("read.txt", "r")

# data = file.readlines()  # -------------> it will convert the new line text into a list
# print(data, type(data))

# file.close()

# # readline using python

# file = open("read.txt", "r")

# line1 = file.readline()  # ------> it will read line by line and give it in string
# print(line1, type(line1))

# line2 = file.readline()
# print(line2, type(line2))

# line3 = file.readline()
# print(line3, type(line3))

# file.close()


# append file in python

# file = open("append.txt", "a")

# write = file.write("my name is abdul samad and i am a good programmer")

# file.close()


# with statement in python

file = open("read.txt", "r")

print(file.read())

file.close()

# the same can be done using with statement

with open("read.txt", "r") as file2:
    print(file2.read())

# the same can be done using with statement and readlines
