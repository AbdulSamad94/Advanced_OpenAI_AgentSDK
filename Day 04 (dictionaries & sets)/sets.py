sets = {}  # empty curly brackets will always be a dictionary
sets = {1, 2, 3, 4, 5}  # this is a set

# to make an empty set we use the set() function like:

sets = set()
print(type(sets))

# why we use set? because we can not have duplicate values in a set
# for example

sets = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(sets)  # {1, 2, 3, 4, 5}

sets.add("Abdul Samad")

print(len(sets))  # 6
sets.remove(1)  # remove 1 from the set
sets.pop()  # remove the random element from the set
sets.clear()  # clear the set
print(sets)  # {1, 2, 3, 4, 5, 'Abdul Samad'}


# Union & InterSection in sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2))  # {4, 5}
