sets = {}  # empty curly brackets will always be a dictionary
sets = {1, 2, 3, 4, 5}  # this is a set

# to make an empty set we use the set() function like:

sets = set()
print(type(sets))

# why we use set? because we can not have duplicate values in a set
# for example

sets = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(sets)  # {1, 2, 3, 4, 5}
