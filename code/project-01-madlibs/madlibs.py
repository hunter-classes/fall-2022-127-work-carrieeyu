"""
MADLIBS EXTRAS:
1)Write a story in a file and read it from your program; include the file in your repo(done)
2)<HERO> would randomly choose a hero once and then use that name for all instances of <HERO>(done)
"""

import random

#creating a list of story elements to use as replacements
verbs = ['talk','walk','run','yell','scream','kick','dance','sit','nap','learn','shout']
nouns = ['school','home','hell','bus','mother','father','river','Bahamas','Hogwarts','snake']
emotions = ['happy', 'grateful', 'fortunate', 'joyful', 'excited', 'prepared']
names = ['carmen', 'Carrie', 'sherry', 'leo', 'ruby', 'Stephen', 'Ben']
heroes = ['h_keith', 'h_shirley', 'h_jen', 'h_chris', 'h_ida', 'h_Xen']

#extra 1
f = open("story.txt", "r") #accessing the text file
theStory = f.read() #reading from the text file
wordsList = theStory.split() #splitting the story into a list struction; to use and access specific words by the index

def substitutions():

  #extra 2
  hero = random.choice(heroes) #generating a random hero ONCE and keeping it consistent throughout the story
  
  for i in range(len(wordsList)): #looping through the words of the story
    if wordsList[i] == "<VERB>":
      wordsList[i] = random.choice(verbs) #random verb for each time <VERB> appears
    if wordsList[i] == "<NOUN>": 
      wordsList[i] = random.choice(nouns) #same idea as random verb
    if wordsList[i] == "<EMOTION>": 
      wordsList[i] = random.choice(emotions) #same idea as random verb
    if wordsList[i] == "<NAME>":
      wordsList[i] = random.choice(names).capitalize() #same idea as random verb
    if wordsList[i] == "<HERO>":
      wordsList[i] = hero.capitalize() #constant hero
    if wordsList[0] == "<VERB>" or "<NOUN>" or "<EMOTION>" or "<NAME>" or "<HERO>":
      wordsList[0] = wordsList[0].capitalize()
  
  return " ".join(wordsList) #reverses back to the original story without access and usage of index

print(substitutions()) #displaying the story's modified version with substitutions

f.close() #closes the story text file
