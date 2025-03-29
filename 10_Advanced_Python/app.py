# lamda function


# def square(e):
#     return e * e

# square = lambda e: e * e  # —————> It will do the same thing as above function

# print(square(4))

# list comprehension

# list = [1, 2, 3, 4, 5]

# squaredList = []

# for i in range(len(list)):
#     squaredList.append(list[i] * list[i])

# print(squaredList)

# squaredList = [i * i for i in list]
# print(squaredList)


# Join

# a = ["hello", "world", "python"]
# b = " ".join(a)
# print(b)

# # map, reduce, filter

# mapList = [1, 2, 3, 4, 5]
# square = lambda e: e * e

# sqList = map(square, mapList)
# print(list(sqList))

# a = [1, 2, 3, 4, 5]
# even = lambda e: e % 2 == 0
# print(list(filter(even, a)))

# from functools import reduce

# a = [1, 2, 3, 4, 5]

# sum = lambda x, y: x + y
# sum = reduce(sum, a)

# print(sum)
