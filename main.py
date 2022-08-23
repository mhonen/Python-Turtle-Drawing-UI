##########################################################################################
#
# Program: Turtle Draw UI
#
# verson: 1.0
#
# Comments: This program draws various shapes using two UI (turtle and tkinter)
#
#########################################################################################

from tkinter import *
from turtle import Turtle, Screen
from draw_shapes import DrawShape as ds # import manual draw class

# Create tkinter window
window = Tk()

window.title("Python Turtle Drawing UI")
window.geometry('640x480')
window.resizable(False, False)
window.config (background='#8da895')

# These methods access the various methods in DrawShape Class
def draw_triangle():
  ds.draw_shapes(3)

def draw_square():
  ds.draw_shapes(4)

def draw_pentagon():
  ds.draw_shapes(5)

def draw_hexagon():
  ds.draw_shapes(6)

def draw_heptagon():
  ds.draw_shapes(7) 

def draw_all():
    ds.draw_everything(3)

def draw_circle():
  ds.draw_circle()

def draw_spiral_graft():
  ds.draw_spiral(20)

# Add one header Label and buttons to main window

main_heading_label = Label(window, bg ='#8da895', font=('Aerial', 15),text="Turtle Drawing Program.", padx=20)
main_heading_label.grid(column=1, row=0)

draw_triangle_button = Button(window, command=lambda: draw_triangle(), text="Draw Triangle")
draw_triangle_button.grid(column=0, row=1, padx = 50, pady=20)

draw_square_button = Button(window, command=lambda: draw_square(), text="Draw Square" )
draw_square_button.grid(column=0, row=2, padx = 50, pady = 20)

draw_pentagon_button = Button(window, command=lambda: draw_pentagon(), text="Draw Pentagon" )
draw_pentagon_button.grid(column=0, row=3, padx = 50, pady = 20)

draw_hexagon_button = Button(window, command=lambda: draw_hexagon(), text="Draw Hexagon" )
draw_hexagon_button.grid(column=1, row=1, padx = 25, pady = 20)

draw_heptagon_button = Button(window, command=lambda: draw_heptagon(), text="Draw Heptagon" )
draw_heptagon_button.grid(column=1, row=2, padx = 25, pady = 20)

draw_circle_button = Button(window, command=lambda: draw_circle(), text="Draw A Circle" )
draw_circle_button.grid(column=1, row=3, padx = 25, pady = 20)

draw_all_button = Button(window, command=lambda: draw_all(), text="Draw All Shapes" )
draw_all_button.grid(column=2, row=1, padx = 25, pady = 20)

draw_spiral_button = Button(window, command=lambda: draw_spiral_graft(), text="Draw Spiral Graph" )
draw_spiral_button.grid(column=2, row=2, padx = 25, pady = 20)

# main window loop.  Click top x to close.
window.mainloop()

