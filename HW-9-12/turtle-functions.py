#Add the following routines:
#hexagon() -- this should have the same parameters as square and triangle but should draw a hexagon.
#ngon(t,numsides,x,y,color,width,sidelen) - this will draw a regular ngon with numsides sides.

import turtle

def hexagon(t,x,y,w,color,sidelen):
    """
    Draw a hexagon using the turtle passed into t
    Parameters:
      t       - a turtle
      x,y     - location
      w       - width of side
      color   - color to draw in
      sidelen - length of each side
    Returns:
      nothing
    """
    # set the location, color, and width
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()
    # draw a hexagon
    for i in range(8):
        t.forward(sidelen)
        t.right(45) #360/8(bc 8 sides in an octagon)


numsides = int(input("Please enter a number of sides for the ngon:"))

def ngon(t,numsides,x,y,color,width,sidelen):
  t.penup()
  t.goto(x,y)
  t.color(color)
  t.width(width)
  t.pendown()

  theSides = int(360/numsides)

  for i in range(numsides):
    t.forward(sidelen)
    t.right(theSides)


wn = turtle.Screen()

crush = turtle.Turtle()
hexagon(crush,-20,30,2,"blue",50)
ngon(crush,numsides,-100,40,"red",5,50)

squirt = turtle.Turtle()
hexagon(squirt,90,100,2,"yellow",30)
ngon(squirt,numsides,50,100,"green",2,50)

wn.exitonclick()
wn.mainloop()