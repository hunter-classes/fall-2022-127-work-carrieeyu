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


v = "yah"

def freq(l,v):
  count = 0
  
  for string in l:
    if string == v:
      count += 1
  return count

result = freq("no","yah")
print("The frequency of the word",v, "is",result,".")