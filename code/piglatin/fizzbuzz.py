#Add a new program named fizzbuzz.py. When run, it should count from 1 to 100. If the number is divisible by 3, print "fizz" if it's divisible by 5 print "buzz" and if it's divisible by 3 and 5, print "fizzbuzz". If it's not divisible by 3 or 5, print the number

"""
for counter in range(1, 101):  
  if (counter % 3 == 0 and counter % 5 == 0):
    print(counter, "fizzbuzz")
  elif (counter % 3 == 0):
    print(counter, "fizz")
  elif (counter % 5 == 0):
    print(counter, "buzz")
  elif (counter % 3 != 0 and counter % 5 != 0):
    print(counter)
"""

def fizzbuzz(n):
  #numer = 1
  #while number < n:
    #print(n)
    #number = number + 1
  for number in range(1,n):
    if number % 3 == 0 and number % 5 == 0:
      print("fizzbuzz")
    elif number % 5 == 0:
      print("buzz")
    elif number % 3 == 0:
      print("fizz")
    else:
      print(number)


def fizzbuzz2(n):
  for number in range(1,n):
    output = ""
    if number % 3 == 0:
      output = output + "fizz"
    if number % 5 == 0:
      output = output + "buzz"
    if output == "":
      output = str(number)
    print(output)
      
value = 20
print("Fizzbuzz up to", value)
fizzbuzz(value)
