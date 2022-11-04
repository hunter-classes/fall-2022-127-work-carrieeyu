#2.8: Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer

radius = int(input("Please enter a radius:"))
pi = 3.14

areaOfCircle = pi*(radius*radius)

print("The area of the circle is", areaOfCircle, ".")
