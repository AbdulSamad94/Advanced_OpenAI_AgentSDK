# Lists & Tuples in Python

randomList = ["Samad", "Abdul", "Rehan", 30, 30.0897, True, False]
print(randomList[0])
randomList[0] = "Abdul Samad"
print(randomList[0])
print(randomList[-1])

randomList.append("Pakistan") #it will add the element at the end of the list
randomList.insert(1, "Karachi") #it will add the element at the given index
randomList.remove("Karachi") #it will remove the element from the list
randomList.pop() #it will remove the last element from the list
randomList.pop(1) #it will remove the element from the given index
randomList.clear() #it will remove all the elements from the list
randomList.extend(["Samad", "Abdul", "Rehan"]) #it will add the elements of the list at the end of the list
randomList.reverse() #it will reverse the list
randomList.sort() #it will sort the list
randomList.copy() #it will copy the list
randomList.count("Samad") #it will return the number of occurrences of the given element
randomList.index("Samad") #it will return the index of the first occurrence of the given element
randomList.remove("Samad") #it will remove the first occurrence of the given element

print(randomList)