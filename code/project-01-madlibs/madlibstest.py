#text file test

import random

verbs = ['talk','walk','nap','yell','scream']
nouns = ['boy','girl','man','woman','cat']
emotions = ['angry','sad','annoyed']

f = open("story.txt")

def substitute(madlibs):
  for word in f:
    word = word.replace("<VERB>", random.choice(verbs))
    word = word.replace("<NOUN>", random.choice(nouns))
    word = word.replace("<EMOTION>", random.choice(emotions))
  return word

word = substitute("story.txt")
print(word) #add another extra and put \n later on to separate each sentence

