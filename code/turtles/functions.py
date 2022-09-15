import turtle
#add the pos turtle to every shape 

def position_turtle(t,x,y,w,color,sidelen):
    t.penup()
    t.goto(x,y)
    t.width(w)
    t.color(color)
    t.pendown()

  
def square(t,x,y,w,color,sidelen):
    """
    Draw a square using the turtle passed into t
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
    # draw a square
    for i in range(4):
        t.forward(sidelen)
        t.right(90)#360/4(bc 4 sides in a square)

def triangle(t,x,y,w,color,sidelen):
    """
    Draw a triangle using the turtle passed into t
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
    #t.penup()
    #t.goto(x,y)
    #t.width(w)
    #t.color(color)
    #t.pendown()
    position_turtle(t,x,y,w,color,sidelen);
    # draw a triangle
    for i in range(3):
        t.forward(sidelen)
        t.right(120)#360/3(bc 3 sides in a triangle)
      #it should be 120 degrees for the EXTERIOR angle, not 60 for the interior angle

    def hexagon(t,x,y,w,color,sidelen):
        ngon(t,6,x,y,w,color,sidelin)
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


#def hexagon(fill in these):
#    #code to draw the hexagon
    
#def ngon(t,numsides,x,y,color,width,sidelen):
#    #code to draw the ngon

wn = turtle.Screen()

crush = turtle.Turtle()

square(crush,0,0,1,"green",50)

squirt = turtle.Turtle()
square(squirt,100,100,5,"red",80)
square(crush,-50,30,3,"yellow",100)
crush.setheading(45)
square(crush,150,30,2,"blue",60)

triangle(crush,-100,-50,2,"green",50)

crush = turtle.Turtle()
hexagon(crush,-20,30,2,"blue",50)
ngon(crush,numsides,-100,40,"red",5,50)

squirt = turtle.Turtle()
hexagon(squirt,90,100,2,"yellow",30)
ngon(squirt,numsides,50,100,"green",2,50)

wn.exitonclick()
wn.mainloop()