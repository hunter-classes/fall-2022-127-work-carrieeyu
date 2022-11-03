"""
MADLIBS EXTRAS:
1)Write a story in a file and read it from your program; include the file in your repo(done)
2)Pay attention to letter case. If you replace a word at the beginning of a sentence, it should be capitalized. Otherwise, lowercase. This is except in the case of proper nouns which should always be capitalized.
"""

import random

#creating a list of story elements to use as replacements
verbs = ['talk','walk','run','yell','scream','kick','dance','sit','nap','learn','shout']
nouns = ['school','home','hell','bus','mother','father','river','Bahamas','Hogwarts','snake']
emotions = ['angry','sad','annoyed','happy','insane','disappointed','confident','desperate']
names = ['Carrie','Julie','Zilena','Carmen','John','Shirley','Ruby','Sherry','Keith']

#extra 1
f = open("story.txt", "r") #accessing the text file
theStory = f.read() #reading from the text file
words = theStory.split()

#this function is used to replace the indicated <> with story elements from the lists that are shown above 
def substitute(madlibs):
  word = theStory
  word = word.replace("<VERB>", random.choice(verbs)) #replaces any indication of <VERB> with an actual verb from the specified list
  word = word.replace("<NOUN>", random.choice(nouns)) #same purpose
  word = word.replace("<EMOTION>", random.choice(emotions)) #same purpose
  word = word.replace("<NAME>", random.choice(names)) #same purpose
  return word #returns all the indicated substitutions of the story
  
  
print(substitute(words)) #displaying the story text with substitutions and prints out a new story
f.close() #closing the text file

