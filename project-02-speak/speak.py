#EXTRAS:
#1) Have an option to translate different languages

f = open("input.txt", "r") #accessing the text file
theStory = f.read() #reading from the text file
wordsList = theStory.split() #splitting the story into a list structure; to use and access specific words by the index

pirate = {'captain' : "cap'n",
          'friends' : "crew",
          'never' : "ne'er",
          'truck' : "schooner",
          'money' : "treasure"}
klistPirate = [x for x in pirate.keys()]
#print(klist)#prints the words before pirate translation and converts to a list

vlistPirate = [x for x in pirate.values()]
#print(vlist)#prints the values of the pirate and converts into a list


brooklyn = {'the' : "de",
            'you' : "yuh",
            'dont' : "doan",
            'to' : "tuh",
            'isnt' : "ain't"}
klistBrooklyn = [x for x in brooklyn.keys()]
#print(klist)#prints the words before pirate translation and converts to a list

vlistBrooklyn = [x for x in brooklyn.values()]
#print(vlist)#prints the values of the pirate and converts into a list

def translatePirate():
    for i in range(len(wordsList)):
      for a in range(len(klistPirate)):
        if wordsList[i] == klistPirate[a]:
          wordsList[i] = pirate.get(klistPirate[a])
    return " ".join(wordsList)

def translateBrooklyn():
    for i in range(len(wordsList)):
      for a in range(len(klistBrooklyn)):
        if wordsList[i] == klistBrooklyn[a]:
          wordsList[i] = brooklyn.get(klistBrooklyn[a])
    return " ".join(wordsList)

chooseLanguage = input("Would you like to translate the story into the Pirate or Brooklyn language?")

if chooseLanguage == "Pirate":
  print(translatePirate())

if chooseLanguage == "Brooklyn":
  print(translateBrooklyn())

f.close()
