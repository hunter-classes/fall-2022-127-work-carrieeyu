s="this is a string"
elist=[]
l1=[12,33,15,20]
l2=['one','two','three']
l3=['one',2,122,33,'something',23]
l4=['one',23,['a','b','c'],5,[10,11,12]]
slice=l1[3:5]
longer_string=s+s
longer_list=l1+l3
#s[5] = 'I' <-- cant do this bc strings are immutable 
#we have to do this:
new_string=s[:5]+'I'+s[6:]#making a new string and then reassigning
#on the other hand, we can change lists directly
l1[4]=9999999

#you can change a list's elements in a function but this generally frowned upon
#since you do not return anything which can be confusing to new programmers
def change_in_place(l,index,new_value):
  l[index]=new_value
print(l1)
change_in_place(l1,4,123)

#this is a slightly better way
def change_in_place_and_return(l,index,new_value):
  """
  this changes l and returns it
  """
  l[index]=new_value
  return l

print(l1)
l2=change_in_place_and_return(l1,4,121)
print(l2)
print(l1)

print("----------------------------------------------------")
#this is an example of aliasing
#it can be powerful but you have to be careful and make sure you're not 
#changing any list that you do not want to change
l2=l1
print("l1:",l1)
print("l2:",l2)
l1[4]=9999
print("l1:",l1)
print("l2:",l2)
print("----------------------------------------------------")
#this is how you usually do a function to change part of a list
#when you want to follow the functional paradige
def change_value(l,index,value):
  #result=[]
  #for item in l:
    #notice we can stick a variable like item in [] to make a list
    #then we can add it on to a result which is a list
    #result = result+[item] 
    #or we can call the list method and append with item as a parameter
    #result.append(item)
  
  #result=l.copy()
  result = 1[:]
  result[index]=value

print(l1)
l2=change_value(l,4,1111)
print("l1:",l1)
print("l2:",l2)