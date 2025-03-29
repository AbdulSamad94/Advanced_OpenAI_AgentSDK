mapList = [1, 2, 3, 4, 5]
square = lambda e: e * e

sqList = map(square, mapList)
print(list(sqList))

a = [1, 2, 3, 4, 5]
even = lambda e: e % 2 == 0
print(list(filter(even, a)))

from functools import reduce

a = [1, 2, 3, 4, 5]

sum = lambda x, y: x + y
sum = reduce(sum, a)

print(sum)
