"""
MADLIBS EXTRAS:
1)Instead of specifying the sentences or story to convert, write a story in a file and read it from your program. Make sure to include the file in your repo and that your program reads it correctly.

2)Pay attention to letter case. That is, if you replace a word at the beginning of a sentence, it should be capitalized, otherwise, lowercase. This is except in the case of proper nouns which should always be capitalized.
"""

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
print(word)







#-------------------------------------------------------NOTES:
"""
import random

verb = "<VERB>"
noun = "<NOUN>"
sentence = "Carrie <VERB> to the <NOUN> because her friend <VERB> to the <NOUN>"

def substitute(verbs,nouns):
  if verb in sentence:
    result = sentence.replace(verb, random.choice(verbs))
  if noun in sentence:
    result2 = result.replace(noun, random.choice(nouns))
  return result2
    
result2 = substitute(['talk','walk','nap','yell','scream'],['boy','girl','man','woman','cat']) #substitution without file_input
print(result2)
"""

