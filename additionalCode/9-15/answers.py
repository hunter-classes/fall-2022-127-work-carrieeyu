#Do Ch 7 numbers 7,8,10, and 11

#7: Write a function called is_even(n) that takes an integer as an argument and returns True if the argument is an even number and False if it is odd.
print("--------------")
print("Even Function:")
print("--------------")

def is_even(n):
  if(n % 2 == 0):
    print ("True")
  else:
    print ("False")

is_even(8)#should print True
is_even(5)#should print False

#8: Now write the function is_odd(n) that returns True when n is odd and False otherwise.
print("--------------")
print("Odd Function:")
print("--------------")

def is_odd(n):
    # your code here
    if n % 2 != 0:
        print ("True")
    else:
        print ("False")

is_odd(8)#should print False
is_odd(5)#should print True

#10: Write a function is_rightangled which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return True if the triangle is right-angled, or False otherwise.
#Hint: floating point arithmetic is not always exactly accurate, so it is not safe to test floating point numbers for equality. If a good programmer wants to know whether x is equal or close enough to y, they would probably code it up as
#if  abs(x - y) < 0.001:      # if x is approximately equal to y
    #...
print("--------------")
print("Right Angle Function:")
print("--------------")

def is_rightangled(a, b, c):
    if abs(c**2-(a**2+b**2) < 0.001):
        print ("True");
    else:
        print ("False");

is_rightangled(3,4,5)#true
is_rightangled(2.3,6.1,10.9)#false
is_rightangled(6,2,8)
is_rightangled(9,2,7)

#11: Extend the above program so that the sides can be given to the function in any order.
print("--------------")
print("Right Angle Extension Function:")
print("--------------")

def is_rightangled(a, b, c):
    if abs(c**2-(a**2+b**2) < 0.001):
        print ("True");
    elif abs(b**2-(a**2+c**2)) < 0.001:
      print ("True");
    elif abs(a**2-(b**2+c**2)) < 0.001:
      print ("True");
    else:
        print ("False");

is_rightangled(3,4,5)#true
is_rightangled(2.3,6.1,10.9)#false
is_rightangled(6,2,8)
is_rightangled(9,2,7)

print("--------- ")
print("Coding Bat")
print("--------- ")
print("1)hello_name")
print("--------- ")

def hello_name(name):
  print("Hello " + name + "!");

hello_name("Carrie")

print("--------- ")
print("2)make_out_word")
print("--------- ")

def make_out_word(out, word):
  print (out[:2] + word + out[2:]);

make_out_word("<<>>","yeah")
make_out_word("{{}}","disappointment")

print("--------- ")
print("3)first_two")
print("--------- ")

def first_two(str):
  if (len(str) == 0):
    print ("");
  else:
    print (str[:2]);

first_two("disappointment")
first_two("air conditioner")
