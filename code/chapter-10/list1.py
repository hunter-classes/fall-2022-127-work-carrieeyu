"""due 10/3 before class"""

#Create a list called myList with the following six items: 76, 92.3, “hello”, True, 4, 76.
prevList = [76, 92.3, "hello", True, 4, 76]

#Append “apple” and 76 to the list.
prevList.append("apple")
prevList.append(76)

#Insert the value “cat” at position 3.
prevList.insert(3, "cat")
#Insert the value 99 at the start of the list.
prevList.insert(0, 99)

#Find the index of “hello”.
indexHello = prevList.index("hello")
print("The index of 'hello' is", indexHello, ".")

#Count the number of 76s in the list.
countSevenSix = prevList.count(76)
print("The number of 76s is", countSevenSix, ".")

#Remove the first occurrence of 76 from the list.
removeSevenSixFirst = prevList.remove(76)
#print("Updated list without first occurrence of 76", removeSevenSixFirst)

#Remove True from the list using pop and index.
indexTrue = prevList.index(True)
removeTrue = prevList.pop(indexTrue)

print(prevList)