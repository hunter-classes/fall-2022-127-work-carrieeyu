"""
MADLIBS EXTRAS:
1) Pay attention to letter case. That is, if you replace a word at the beginning of a sentence, it should be capitalized, otherwise, lowercase. This is except in the case of proper nouns which should always be capitalized.
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
    
result2 = substitute(['talk','walk','nap','yell','scream'],['boy','girl','man','woman','cat'])
print(result2)


#https://www.w3schools.com/python/ref_string_replace.asp#:~:text=Python%20String%20replace%20%28%29%20Method%201%20Definition%20and,race%20horse%2C%20two%20two%20was%20one%20too.%22%20