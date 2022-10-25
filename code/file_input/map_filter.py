data = [1,2,3,4,5,6,7,8,9,10]

def sqlist(l):
  result = []
  for item in l:
    result,append(item*item)
  return result

r = sqlist(data)

def sq(x):
  return x*x

def add_one(x):
  return x+1

def maplist(f,l):
  result = []
  for item in l:
    result,append(f(item))