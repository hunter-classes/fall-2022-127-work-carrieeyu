#text file test
import random

verbs = ['talk','walk','run','yell','scream']
nouns = ['school','home','hell']
emotions = ['angry','sad','annoyed','happy','insane']
names = ['Carrie','Julie','Zilena','Carmen','John']

f = open("story.txt", "r")
#sentences = f.read()
#words = sentences.split()

def substitute(madlibs):
  for word in f:
    word = word.replace("<VERB>", random.choice(verbs))
    word = word.replace("<NOUN>", random.choice(nouns))
    word = word.replace("<EMOTION>", random.choice(emotions))
    word = word.replace("<NAME>", random.choice(names))
  return word

def capitalize():
  for word in f:
    if "<VERB>" or "<NOUN>" or "<EMOTION>":
      word.capitalize()
    if words == "<NAME>":
      word.capitalize()
  return word
      
word = substitute("story.txt")
print(word)