def bondify(name):
  """
  Input string in the form “first last”
	Return “Last, first last”
  """
  result1 = ""
  location = name.find(' ') #finds the space between first and last
  first = name[:location].capitalize() #everything before the space between last and first
  last = name[location+1:].capitalize() #everything after the space between last and first

  result1 = last + ", " + result1 + first + " " + last
  
  return result1 #need this or it will print "none"

result1 = bondify("james bond")
print("james bond -->", result1)

print("----------------------------------------------------")


def piglatin(word):
  """
  input: a string representing a word
  returns: a new string with the word converted to piglatin
  
  Rules:
  if the first letter is a consonent, move it from the start to the
  end and add "ay" 
  so "hello" becomes "ellohay"
  
  If the first letter is a vowel, just add "yay" to the end 
  try to also handle upper case words
  """

  firstLetter = word[0] #getting first letter
  noFirstLetter = word.strip(firstLetter) #strip method removes first letter

  result2 = "" #empty string

  if(firstLetter == "a" or firstLetter == "e" or firstLetter == "i" or
     firstLetter == "o" or firstLetter == "u" or firstLetter == "A" or
     firstLetter == "E" or firstLetter == "I" or firstLetter == "O" or
     firstLetter == "U"):
       
    result2 = word + "yay"; #first letter that is a vowel
    return result2 #need this or it will print "none"
  else:
    result2 = noFirstLetter + firstLetter + "ay"; #first letter that is a consonant
    return result2 #need this or it will print "none"

result2 = piglatin("Aurys")
print("Aurys -->",result2)

result2 = piglatin("octopus")
print("octopus -->",result2)

result2 = piglatin("igloo")
print("igloo -->",result2)

result2 = piglatin("Hogwarts")
print("hogwarts -->",result2)

result2 = piglatin("hello")
print("hello -->", result2)


#9/22/2022 homework; modify the capital letters 
#alternative solution
#To DO:
#1. Make it work for capitalized words
#ex. Cable --> Ablecay
#Able --> Ableay. & cable. --> ablecay.


#if Cable --> Ablecay

def piglatinfy(word):
  first = word[0]
  
  if first in 'aeiou' and first[0].islower():
    result = word + 'ay'
  elif first in 'AEIOU' and first[0].isupper():
    result = word[1:].capitalize() + first.lower() + 'ay'
  elif first[0].isupper():
    #move first letter to end and add 'ay'
    result = word[1:].capitalize() +first.lower()+'ay'
  else:
    result = word[1:]+first.lower()+'ay'
    
  return result

test_word = "hello"
result = piglatinfy(test_word)
print(test_word,"-->",result)


test_word = "Cable"
result = piglatinfy(test_word)
print(test_word,"-->",result)


test_word = "Able."
result = piglatinfy(test_word)
print(test_word,"-->",result)


