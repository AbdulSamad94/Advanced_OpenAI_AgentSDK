list = [1, 2, 3, 4, 5]

squaredList = []

for i in range(len(list)):
    squaredList.append(list[i] * list[i])

print(squaredList)

squaredList = [i * i for i in list]
print(squaredList)
