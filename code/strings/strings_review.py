# use for different python methods: https://www.w3schools.com/python/ref_string_find.asp
#use to run code and has the breakdown of each line: https://pythontutor.com/
#python problem practice: https://codingbat.com/python

s1 = "Hello World"

s2 = 'another\nstring' #skipping to another line

s3 = """
This is a multiline string
we use the triple quotes
for those
"""
s4 = s1 + s1 #string catenation

print(s4)
print(s1*3)
print(3*s1)
#s4 = s1 + 4 cannot concatenate a string and an int

print(len(s1))
print(len("abcde"))

print(s1.upper())

print(s1.find("o"))

print(s1[0:5])#include 0 but not 5
print(s1[5:10])#include 5 but not 10
#print([:5])#means from the beginning..?
print(len(s1))
print(s1.find(" "))

space_location = s1.find(" ")
print(space_location)
#pulls out 6(one after the space) until the end and s5 = s1[sapce_location+1:len(s1)]
s5 = s1[sapce_location+1]#nothing after the : means go to the end 
print(s5)
print(s1[-1])



