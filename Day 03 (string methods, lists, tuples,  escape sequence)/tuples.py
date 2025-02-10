# Tuples in Python

tuple = ("Samad", 45, 61, 78.98, True, None, "Abdul", "Samad")
# print(tuple)

tuple2 = ("Hello", "World")
concatTuple = tuple + tuple2
print(concatTuple)

no = tuple.count("Samad")
# print(no)

falseNo = tuple.count(3)
print(falseNo)

index = tuple.index(True)
print(index)

falseIndex = tuple.index("hello")
print(falseIndex)

print(2 in concatTuple)  # True or False
print(100 in concatTuple)  # True or False
