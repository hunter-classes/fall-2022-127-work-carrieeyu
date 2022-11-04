"""
MADLIBS EXTRAS I HAVE COMPLETED:
1)Write a story in a file and read it from your program; include the file in your repo
2)<HERO> would randomly choose a hero once and then use that name for all instances of <HERO>
3)Placed capitalization where it should be; the beginning of a sentence and nouns
"""

import random

#creating a list of story elements to use as replacements for <>
verbs = ['talk','walk','run','yell','scream','kick','dance','sit','nap','learn','shout']
nouns = ['school','home','hell','bus','mother','father','river','bahamas','hogwarts','snake']
emotions = ['happy', 'grateful', 'fortunate', 'joyful', 'excited', 'prepared']
names = ['carmen', 'carrie', 'sherry', 'leo', 'ruby', 'stephen', 'cen']
heroes = ['h_keith', 'h_shirley', 'h_jen', 'h_chris', 'h_ida', 'h_Xen']

#EXTRA 1
f = open("story.txt", "r") #accessing the text file
theStory = f.read() #reading from the text file
wordsList = theStory.split() #splitting the story into a list structure; to use and access specific words by the index

def substitutions():

  #EXTRA 2
  hero = random.choice(heroes) #generating a random hero ONCE and keeping it consistent throughout the story
  
  for i in range(len(wordsList)): #looping through the words of the story
    if wordsList[i] == "<VERB>":
      wordsList[i] = random.choice(verbs) #random verb for each time <VERB> appears
    if wordsList[i] == "<NOUN>": 
      wordsList[i] = random.choice(nouns) #same idea as random verb
    if wordsList[i] == "<EMOTION>": 
      wordsList[i] = random.choice(emotions) #same idea as random verb
    if wordsList[i] == "<NAME>":
      #EXTRA 3
      wordsList[i] = random.choice(names).capitalize() #same idea as random verb and also converts the name's first letter to uppercase
    if wordsList[i] == "<HERO>":
      #EXTRA 3
      wordsList[i] = hero.capitalize() #constant hero
    if wordsList[0] == "<VERB>" or "<NOUN>" or "<EMOTION>" or "<NAME>" or "<HERO>":
      wordsList[0] = wordsList[0].capitalize() #capitalizes any category's elements if it appears in the first index of the story
  
  return " ".join(wordsList) #changes back to the structure of the original story; no longer a list of words

print(substitutions()) #displaying the story's modified version with substitutions

f.close() #closes the story text file
