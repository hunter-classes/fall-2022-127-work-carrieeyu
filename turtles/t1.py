import turtle 

def sample_function():
  print("This is a function")
  print("it can be used multiple times")
  
wn = turtle.Screen() #making turtle window

crush = turtle.Turtle() #making a turtle

#to draw a square

#manually
#crush.forward(50)
#crush.right(90)

#crush.forward(50)
#crush.right(90)

#crush.forward(50)
#crush.right(90)

#crush.forward(50)
#crush.right(90)

#for-loop way
for i in range(4):
  crush.forward(50)
  crush.right(90)

#create a second turtle 
#into the variable squirt
#and make squirt draw a triangle

squirt = turtle.Turtle()

#to draw a triangle
squirt.up()
squirt.goto(100,100)
squirt.down()
squirt.color("green")
squirt.width(5)

#manually
#squirt.right(50)
#squirt.right(120)

#squirt.forward(50)
#squirt.right(120)

#squirt.forward(50)
#squirt.right(120)

#for-loop way
for i in range(3):
  squirt.forward(50)
  squirt.right(120)
  
sample_function()
sample_function()
sample_function()


wn.exitonclick() #when the white box with the turtle is clicked, it will exit out of that turtle program
wn.mainloop()