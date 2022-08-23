######################################################################################
#
# Class: DrawShape
#
# Comments: Contains attributed and methods to draw shapes.
#
######################################################################################

from turtle import Turtle, Screen, speed
import random

class DrawShape():
  # Constructor
  def __init__(self,numsides):
    self.sides = numsides
    self.size_of_gap = numsides;

  #Takes in number of sides and draws the correct shape i.e. 360/3 = Triangle, 360/4 = square, etc.
  def draw_shapes(sides):
    t = Turtle()
    s = Screen()
    colours = ['red', 'green', 'blue', 'green', 'orange', 'black', 'lightblue', 'purple']
    t.color(random.choice(colours))
    for _ in range(sides):
      angle = (360 / sides)
      t.forward(100)
      t.right(angle)

    s.exitonclick()

  # Draws all shapes with sides i.e. no circles
  def draw_everything(sides):
    t = Turtle()
    s = Screen()
    colours = ['red', 'green', 'blue', 'green', 'orange', 'black', 'lightblue', 'purple']
    for x in range(3,10):
      for _ in range(x):
        t.color(random.choice(colours))
        angle = (360 / x)
        t.forward(100)
        t.right(angle)

    s.exitonclick()

  # Draw one circle
  def draw_circle():
    t = Turtle()
    s = Screen()
    colours = ['red', 'green', 'blue', 'green', 'orange', 'black', 'lightblue', 'purple']
    t.color(random.choice(colours))
    t.circle(100)

    s.exitonclick()

  # draws a lot circles into a 360 arc.  Space between circles depends on size_of_gap passed in.
  def draw_spiral(size_of_gap):
    t = Turtle()
    s = Screen()
    colours = ['red', 'green', 'blue', 'green', 'orange', 'black', 'lightblue', 'purple']

    for _ in range(int(360 / size_of_gap)):
      t,speed('fastest')
      t.color(random.choice(colours))
      t.circle(100)
      t.setheading(t.heading() + size_of_gap)

    s.exitonclick()