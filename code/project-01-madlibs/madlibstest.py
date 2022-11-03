#text file test

"""
import random

verbs = ['talk','walk','nap','yell','scream']
nouns = ['boy','girl','man','woman','cat']

f = open("story.txt", "r")
madlibsStory = f.read()
words = madlibsStory.split()

def change_verb(data):
  x = " "
  for i in range(len(words)):
    if words[i] == "<VERB>":
      x += (" " + random.choice(verbs))
  return x

#print(change_verb("story.txt"))
result = change_verb("story.text")
print(result)
"""




"""

import random

verbs = ['talk','walk','nap','yell','scream']
nouns = ['boy','girl','man','woman','cat']

f = open("story.txt", "r")
madlibsStory = f.read()
words = madlibsStory.split()

print(" ".join(words))


for i in range(len(words)):
  if words[i] == "<VERB>":
    words[i] = words[i].replace("<VERB>", random.choice(verbs))
  print(words)


f.close()
"""

"""
import random

verbs = ['talk','walk','run','yell','scream']
nouns = ['school','home','hell']
emotions = ['angry','sad','annoyed','happy','insane']
names = ['Carrie','Julie','Zilena','Carmen','John']

f = open("story.txt")

def substitute(madlibs):
  for word in f:
    word = word.replace("<VERB>", random.choice(verbs))
    word = word.replace("<NOUN>", random.choice(nouns))
    word = word.replace("<EMOTION>", random.choice(emotions))
    word = word.replace("<NAME>", random.choice(names))
  return word

word = substitute("story.txt")
print(word)
#print(word.capitalize()) #fix b/c capitalizes the first word and puts everything else in lower case


f.close()
"""



"""
PRINTS TWO LINES FROM STORY without split method

import random

verbs = ['talk','walk','run','yell','scream']
nouns = ['school','home','hell']
emotions = ['angry','sad','annoyed','happy','insane']
names = ['Carrie','Julie','Zilena','Carmen','John']

f = open("story.txt", "r")
theStory = f.read()
print(theStory)

f.close()
"""

import random

verbs = ['talk','walk','run','yell','scream']
nouns = ['school','home','hell']
emotions = ['angry','sad','annoyed','happy','insane']
names = ['Carrie','Julie','Zilena','Carmen','John']

f = open("story.txt", "r")
theStory = f.read()
listStory = theStory.split("\n")

def substitute(data):
  for i in range(len(listStory)):
    if listStory[i] == "<VERB>":
      listStory[i] = listStory[i].replace("<VERB>", random.choice(verbs))
    #return " ".join(listStory)
    return listStory[i]


print(" ".join(listStory))
#print(theStory)
i = substitute("story.txt")
print(i)

f.close()