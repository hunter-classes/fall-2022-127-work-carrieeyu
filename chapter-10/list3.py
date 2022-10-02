"""due 10/6 before class"""

#Number 5: Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value. (Note: there is a builtin function named max but pretend you cannot use it.)
def maxNum(numsList):
  max = 0
  
  for num in numsList:
    if num > max:
      max = num
  return max

result = maxNum([1,9,3])
print("The max number is",result,".")

result = maxNum([678,100,4356,235])
print("The max number is",result,".")

result = maxNum([1,1,1])
print("The max number is",result,".")

print("---------------------------------------------")

#Number 7: Write a function to count how many odd numbers are in a list.
def countOdd(numsList):
  count = 0

  for num in numsList:
    if num%2 == 1:
      count += 1
  return count

result = countOdd([1,2,3])
print("The number of odd numbers is",result,".")

result = countOdd([1,9,11])
print("The number of odd numbers is",result,".")

result = countOdd([0,2,4])
print("The number of odd numbers is",result,".")

print("---------------------------------------------")

#Number 8: Sum up all the even numbers in a list.
def sumOfEven(numsList):
  sum = 0

  for num in numsList:
    if num%2 == 0:
      sum += num
  return sum

result = sumOfEven([1,2,4])
print("The sum of even numbers is",result,".")

result = sumOfEven([8,2,4])
print("The sum of even numbers is",result,".")

result = sumOfEven([1,1,3])
print("The sum of even numbers is",result,".")