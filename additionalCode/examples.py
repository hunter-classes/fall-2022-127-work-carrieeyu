#right triangle code from 9/15 hw
def isRightAngle(a,b,c):
  """
  c is longest
  """
  #return abs(math.sqrt(sum)-c)) < 0.001
  return a*a + b*2 == c*c
  
def isRightAngle2(a,b,c):
  """
  any order of the sides
  """
  return isRightAngle(a,b,c) or isRightAngle(b,c,a) or isRightAngle(a,c,a)

#\ means continuing to next line from previous



def is_even(n):
#pass #placeholder to put in a value of the function later when you have not called it to to run(is_even(n)) but want to run other functions without errors
  if n%2==0:
    return True
  else:
    #print(False) #will result in output None when you run it
    return False

def is_even_short_version(n):
  return n%2==0

def is_odd(n):
  return not(is_even(n)) #returns the opposite result of is_even's code

print("Even tests")
result = is_even(10)
print("Result for 10 is:", result)
result = is_even(11)
print("Result for 11 is:", result)
#none in python means null in Java

print("Odd tests")
result = is_odd(10)
print("Result for 10 is:", result)
result = is_odd(11)
print("Result for 11 is:", result)

print("Direct call:", is_even(11))

print("Direct Call short version:", is_even_short_version(15))
print("Direct Call short version:", is_even_short_version(16))

print(isRightAngle(5,3,4))
print(isRightAngle)

def initialize(name):
  """
  Input a string in the form “first last”
  Return a string in the form “F. Last”
  """
  result = ""
  #isolate uppercase and add first init to result
  first = name[0]
  first = first.upper()
  result = result + first + "."

  #find the last name
  location = name.find(' ')
  last = name[location+1:].capitalize()
  result = result + ' ' + last
  
  return result



def bondify(name):
  """
  Input string in the form “first last”
	Return “Last, first last”
  """
  result1 = ""
  location = name.find(' ')
  first = name[:location].capitalize() #everything before the space between last and first
  last = name[location+1:].capitalize() #everything after the space between last and first

  result1 = last + ", " + result1 + first + " " + last
  
  return result1


result = initialize("james bond")
print("james bond -->", result)

result1 = bondify("james bond")
print("james bond -->", result1)






#using return in replit might not show an output while print will but don't use it
#only use print when you want something to appear to the screenof someone using your program, such as questions for input