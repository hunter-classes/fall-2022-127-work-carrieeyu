#You can name the functions anything you wish.

#Number 1: Write a function to find the smallest value in a listKfind smallest in a list of items
print("(1)")

def minNum(numsList):
  min = numsList[0]
  
  for num in numsList:
    if num < min:
      min = num
  return min

result = minNum([1,9,3])
print("The min number is",result,".")

result = minNum([678,100,4356,235])
print("The min number is",result,".")

result = minNum([1,1,1])
print("The min number is",result,".")

print("------------------------------------")

#Number 2: Write a function that returns a new list that contains
#all the odd items in the original list
print("(2)")

def oddNum(numsList):
  newList = []

  for num in numsList:
    if num % 2 == 1:
      newList.append(num)
  return newList
    
result = oddNum([1,2,3,4,5,6])
print("The odd numbers are",result,".")

result = oddNum([2,4,6,8,0,20])
print("The odd numbers are",result,".")

result = oddNum([7,2,7,4,1,10593])
print("The odd numbers are",result,".")

print("------------------------------------")
#Number 3: Write a function that takes a string and returns a new string where all the words are capitalized.
print("(3)")

def stringCaps(string):
  newString = string.capitalize()
  return newString
  
result = stringCaps("i don't like school")
print("The capitalized version of the string is,",result,".")

result = stringCaps("yolo")
print("The capitalized version of the capitalized is,",result,".")

result = stringCaps("woohoo no more homework")
print("The capitalized version of the capitalized is,",result,".")

print("------------------------------------")
#Number 4: Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case
print("(4)")

def longerThanFive(string):
  if len(string) > 5:
    newString = string.upper()
  else:
    newString = "the string is not longer than 5 characters"
  return newString

result = longerThanFive("no more homework")
print("The upper case version of the word is,",result,".")

result = longerThanFive("no")
print("The upper case version of the word is,",result,".")

result = longerThanFive("period")
print("The upper case version of the word is,",result,".")

print("------------------------------------")
#Number 5: Write a function that takes a list of numbers and returns a new list with each item squared
print("(5)")

def squaredNum(numsList):
  squaredList = []
  
  for num in numsList:
    squaredList.append(num**2)
  return squaredList

result = squaredNum([1,2,3,4])#-->should return 1,4,9,16
print("The squared numbers",result,".")

result = squaredNum([2,4,9,10])#-->should return 4,16,81,100
print("The squared numbers",result,".")

result = squaredNum([7,12,10,25])#-->should return 49,144,100,625
print("The squared numbers",result,".")

print("------------------------------------")
#Number 6: Write a function that takes two lists of numbers and returns a new
#list where each item is the corresponding values of the original lists added together. 
#Ex [1,2,3] and [10,20,30] would return the list [11,22,33]
print("(***6)")

def addLists(list1, list2):
  num = 0
  newList=[]

  for number in list1:
    newList.append(number+list2[num])
    num += 1
  return newList
  
result = addLists([4,1,0],[1,1,4])
print("The combined list of added numbers are",result,".")

result = addLists([3,1],[2,4])
print("The combined list of added numbers are",result,".")

result = addLists([1,8,1,10],[1,2,3,4])
print("The combined list of added numbers are",result,".")

#Number 7: Ch 10:#10; Count how many words in a list have length 5.
print("(7, Ch 10:#10)")

def countFive(numsList):
  count = 0

  for num in numsList:
    if len(num) == 5:
      count += 1
  return count

result = countFive(["apple","banana","carrot","watermelon","pear"])
print("The number of words with a length of 5 is",result,".")

result = countFive(["carrie","emily","sarah","venus","carah"])
print("The number of words with a length of 5 is",result,".")

result = countFive(["mug","spray","eraser","lotion","kayla"])
print("The number of words with a length of 5 is",result,".")

print("------------------------------------")
#Number 8: Ch 10:#11; Sum all the elements in a list up to but not including the first even number.
print("(***8, Ch 10:#11)")

"""
def noFirstEven(numsList):

  sum = 0

  for num in numsList:
    if num % 2 == 0:
      numsList.remove(num)
      sum += num
  return sum


result = noFirstEven([1,2,3,4])#-->should return 8
print("The sum without the first even number is",result,".")

result = noFirstEven([1,1,1,1,])#-->should return 4
print("The sum without the first even number is",result,".")

result = noFirstEven([2,3,43,1])#-->should return 47
print("The sum without the first even number is",result,".")
"""

print("------------------------------------")
#Number 9: Ch 10:#12; Count how many words occur in a list up to and including the first occurrence of the word “sam”.
print("(***9, Ch 10:#12)")

"""
def countToSam(listNums):

  count = 0;

  for string in listNums:
    if string == "sam":
      count += 1
  return count
  
result = countToSam(["no","yes","sam","dude","what"])#should return 3 bc there are two words before and including sam
print("The number of times sam occurs in the list is",result,".")

result = countToSam(["sam","sam","sam","school","sam"])
print("The number of times sam occurs in the list is",result,".")

result = countToSam(["sam","sam","what"])
print("The number of times sam occurs in the list is",result,".")
"""