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


#dataset = buildRandomList(20,30)

def testMode(size,maxValue):
  dataset = 