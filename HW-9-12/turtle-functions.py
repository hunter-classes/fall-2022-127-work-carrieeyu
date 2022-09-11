#Add the following routines:
#hexagon() -- this should have the same parameters as square and triangle but should draw a hexagon.
#ngon(t,numsides,x,y,color,width,sidelen) - this will draw a regular ngon with numsides sides.

#Make sure to put tests in your program so when it runs it draws everything.

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


#def hexagon(fill in these):
#    #code to draw the hexagon
    
#def ngon(t,numsides,x,y,color,width,sidelen):
#    #code to draw the ngon

wn = turtle.Screen()

octy = turtle.Turtle()

hexagon(octy,-50,30,2,"blue",50)

wn.exitonclick()
wn.mainloop()