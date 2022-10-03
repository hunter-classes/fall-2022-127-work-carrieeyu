"""due 10/3 before class"""

#Number 4: Write a function called average that takes a list of numbers as a parameter and returns the average of the numbers.
"""
def average(listNums):
  sum = 0
  
  for num in listNums:
    sum += num

  return sum/len(listNums)
"""

                                    #or
  
def average(l):
  sum=0 
  
  for item in l:
    sum += item

  average = sum/len(l)
  return average

result = average([1,2,3])
print("The average is",result,".")#should be 2

result = average([3,3,3])
print("The average is",result,".")#should be 3

result = average([4,5,10])
print("The average is",result,".")#should be 6.3......

#Number 6: Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs. For example, sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
"""
def sum_of_squares(xs):
  sum = 0

  for num in xs:
    sum += num**2

  return sum
"""

def sum_of_squares(l):
  sum=0
  for item in l:
    sum = sum + item*item
  return sum

result = sum_of_squares([2,3,4])
print("The average is",result,".")#should be 29

result = sum_of_squares([1,2,3])
print("The average is",result,".")#should be 14

result = sum_of_squares([4,9,10])
print("The average is",result,".")#should be 197