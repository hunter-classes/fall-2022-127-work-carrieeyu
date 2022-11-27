#SOLO PROJECT
#EXTRAS:
#1) Have an option to translate different languages **DONE-->option to choose Pirate, Brooklyn, or nonsenseAbbreviate(made-up language)
#2) Advanced translations **DONE

f = open("input.txt", "r") #accessing the text file
theStory = f.read() #reading from the text file
wordsList = theStory.split() #splitting the story into a list structure; to use and access specific words by the index

#creating the Pirate dictionary
pirate = {'captain' : "cap'n",
          'friends' : "crew",
          'never' : "ne'er",
          'truck' : "schooner",
          'money' : "treasure"}

klistPirate = [x for x in pirate.keys()]#converts to a list of words before Pirate translation

pirateWords = ['shiver me timbers!', 'blimey!', 'sink me!']
brooklynWords = ['it is real sad!', 'got me dumbfounded!']
nonsenseWords = ["n'more!", 'cryin!', 'weepin!']

#creating the Brooklyn dictionary
brooklyn = {'the' : "de",
            'you' : "yuh",
            "don't" : "doan",
            'to' : "tuh",
            "isn't" : "ain't"}

klistBrooklyn = [x for x in brooklyn.keys()]#converts to a list of words before Brooklyn translation

#creating the nonsenseAbbreviate dictionary
nonsenseAbbreviate = {'surrounded' : "surr'nded",
                      'friends' : "fre'ns",
                      'looked' : "lo'ked",
                      'truck' : "tr'ck",
                      'money' : "m'ney"}

klistNonsenseAbbreviate = [x for x in nonsenseAbbreviate.keys()]#converts to a list of words before nonsenseAbbreviate translation

import random

#function translates into Pirate language
def translatePirate():
    for i in range(len(wordsList)):#nested for-loop to go through each word of the story
      for a in range(len(klistPirate)):#and to go through each word of dict before Pirate translation
        if wordsList[i] == klistPirate[a]:#finds which key words match the story words
          wordsList[i] = pirate.get(klistPirate[a])#converts the key words into Pirate language by getting the value
        if wordsList[i] == "<phrase>":
          wordsList[i] = random.choice(pirateWords)
    return (" ".join(wordsList).capitalize())#changes back to the structure of the original story; no longer a list of words

#function translates into Brooklyn language; same process as Pirate function
def translateBrooklyn():
    for i in range(len(wordsList)):
      for a in range(len(klistBrooklyn)):
        if wordsList[i] == klistBrooklyn[a]:
          wordsList[i] = brooklyn.get(klistBrooklyn[a])
        if wordsList[i] == "<phrase>":
          wordsList[i] = random.choice(brooklynWords)
    return (" ".join(wordsList).capitalize())

#function translates into nonsenseAbbreviate language; same process as Pirate function
def translateNonsenseAbbreviate():
    for i in range(len(wordsList)):
      for a in range(len(klistNonsenseAbbreviate)):
        if wordsList[i] == klistNonsenseAbbreviate[a]:
          wordsList[i] = nonsenseAbbreviate.get(klistNonsenseAbbreviate[a])
        if wordsList[i] == "<phrase>":
          wordsList[i] = random.choice(nonsenseWords)
    return (" ".join(wordsList).capitalize()) 


chooseLanguage = input("Would you like to translate the story into the Pirate, Brooklyn, or nonsenseAbbreviate language?")#user input to pick language

if chooseLanguage == "Pirate" or chooseLanguage == "pirate" or chooseLanguage == "PIRATE":
  print("\n", translatePirate())#utilizes Pirate language if user picks Pirate

if chooseLanguage == "Brooklyn" or chooseLanguage == "brooklyn" or chooseLanguage == "BROOKLYN":
  print("\n", translateBrooklyn())#utilizes Brooklyn language if user picks Brooklyn

if chooseLanguage == "nonsenseAbbreviate" or chooseLanguage == "nonsense abbreviate" or chooseLanguage == "nonsense Abbreviate" or chooseLanguage == "NonsenseAbbreviate" or chooseLanguage == "Nonsense abbreviate" or chooseLanguage == "Nonsenseabbreviate" or chooseLanguage == "nonsenseabbreviate" or chooseLanguage == "NONSENSEABBREVIATE":
  print("\n", translateNonsenseAbbreviate())#utilizes nonsenseAbbreviate language if user pics nonsenseAbbreviate

f.close()
