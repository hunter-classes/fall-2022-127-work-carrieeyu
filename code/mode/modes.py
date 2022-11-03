#Q1: findLargest(l) which takes in a list of numbers and returns the value of the smallest number

def findLargest(l):
  min = l[0]
  
  for num in l:
    if num < min:
      min = num
  return min

result = findLargest([2,5,3])
print("The min number is",result,".")

result = findLargest([678,100,4356,235])
print("The min number is",result,".")

result = findLargest([1,1,1])
print("The min number is",result,".")

print("---------------------------------------------")
#Q2: freq(l,v) which takes a list of numbers (l) and a value (v). The function will return the freuqeency of v, that is, the number of times that v appears in l.

def freq(l,v):

#shortcut:
#return l.count("yah")
  
  count = 0

  for string in l:
    if string == v:
      count += 1
  return count

result = freq(["weewoo","yah","weewoo","yeet","yah"],"weewoo")
print("The frequency of the word","is",result,".")

result = freq(["no","yah","okay","yeethay"],"yah")
print("The frequency of the word","is",result,".")

result = freq(["no","keke","okay","carrie"],"amongus")
print("The frequency of the word", "is",result,".")

#------------------------------------------------------

import random
import datetime

def mode(dataset):
    """
    Returns a mode of the dataset, that is
    the value that appears most frequently
    if multiple values appear the same # of times and are
    most frequent, return any of them.
    Ex: mode([5,4,5,6,7,8,5,4]) --> 5 since 5 appears the most
    mode([5,5,5,4,4,4,2,2,7,7,8,8,9]) --> return 5 or 4 since
    both of those values appear 3 times which is the most
    Strategy:
    assume the first value is the mode
    we can grab its frequency
    for each remaining item in the dataset:
      count that items frequence and see if it's the new
      mode so far    
    """
    modeSoFar = dataset[0]
    freqSoFar = freq(dataset,modeSoFar)
    for item in dataset[1:]:
        if freq(dataset,item) > freqSoFar:
            modeSoFar = item
            freqSoFar = freq(dataset,item)
            
    return modeSoFar

def freq(dataset,v):
    # since this loops over the
    # entire data set once
    # it takes n time 
    #count = 0
    #for item in dataset:
    #    if item == v:
    #        count = count + 1
    #return count
    return len([x for x in dataset if x == v])

def buildRandomList(size,maxvalue):
    #result = []
    #for x in range(size):
    #    result.append(random.randrange(maxvalue))
    #return result
    result = [random.randrange(maxvalue) for x in range(size)]
    return result 

def fastMode(dataset):
    # assume all values in dataset
    # are between 0 and 99 inclusive

    # 1. make a list of 100 slots and set them all to 0 this will store our tallies
    talliesList = [0]*100

    # 2. Loop through our dataset and for each item incremement (add 1) to the appropriate slot in the tallies list
    for i in dataset(tally):
      talliesList += 1

    # 3. the index with the highest value in tallies is the mode
    max = tally[0]
  
    if i > max:
      max = i
    return max
  
    print(talliesList)

def testMode(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = mode(dataset)
    print("Mode: ",m)

def testFindLargest(size,maxValue):
    print("Dataset Size: ",size)
    dataset = buildRandomList(size,maxValue)
    # print(dataset)
    m = findLargest(dataset)
    print("Largest: ",m)

#testFindLargest(80000,30)
testMode(40000,30)

