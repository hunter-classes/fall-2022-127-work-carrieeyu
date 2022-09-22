import random


#this is a foreach loop
for counter in range(2,20,3):
  print(counter)

print("--------------")

#this is a foreach loop
for counter in range(5): #prints 0-4 and not 5; generates a list of items 
  print(counter)

print("--------------")

for letter in "this is a sentence": #prints each letter and space in a new line down vertically
  print(letter)

#while loop
loop_counter = 0 
  
while random.randrange (0,100)<80:
  print("hello", loop_counter)
  loop_counter = loop_counter + 1
print("The above loop ran this many times: ", loop_counter)

#while loop as a counting loop
#first set up a cariable to hold the count
i = 0
#then use the boolean to indicate when to stop
while i < 5:
  print(i)
  i = i + 1 #don't forget to change the variable so you eventually stop
print("--------------")
#count down
i = 5 
while i > 0:
  print(i)
  i = i - 1 #don't forget to change the variable so you eventually stop

#you can traverse over a string
s = "hello world"
t = 0
while i < len(s):
  print(s[i])
  i = i + 1
print("--------------")
#does the same thing except this time with a for loop
for i in range(len(s)):
  print(s[i])