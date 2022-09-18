def bondify(name):
  """
  Input string in the form “first last”
	Return “Last, first last”
  """
  result1 = ""
  location = name.find(' ')
  first = name[:location].capitalize() #everything before the space between last and first
  last = name[location+1:].capitalize() #everything after the space between last and first

  result1 = last + ", " + result1 + first + " " + last
  
  return result1

result1 = bondify("james bond")
print("james bond -->", result1)