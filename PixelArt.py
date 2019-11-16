#Pixel Art Program
#Create simple pixel art

#Made by Naomi Lewis through Python 3.7.4

import graphics
from graphics import *

import tkinter

#----------Parameters----------

rows = 100
cols = 100

size = 7
margin = 50


#----------Start Screen----------

win = GraphWin("PixelArt", 600,600)
win.setBackground(color_rgb(255, 255, 255))

start = Text(Point(275,275), "Click here to start drawing")
start.draw(win)

box = Rectangle(Point(150,225), Point(400,325))
box.draw(win)

win.getMouse()

#----------Undraw Start Screen----------

start.undraw()
box.undraw()

#----------Grid----------

for i in range(1,100):
    vline = Line(Point(0,(i * size)),
                 Point((cols * size), (i * size)))
    vline.setWidth(1/5)
    vline.setOutline(color_rgb(0,0,0))
    vline.draw(win)

for i in range(1,100):
    hline = Line(Point((i * size), 0),
                  Point((i *size), (rows * size)))
    hline.setWidth(1/5)
    hline.setOutline(color_rgb(0,0,0))
    hline.draw(win)

#----------Coloring---------- (incomplete)

#Drop-down Menu
options = tkinter.StringVar(win)

colors = ["black","gray","silver","whitesmoke","rosybrown","firebrick",
          "red","darksalmon","sienna","sandybrown"] #will add on later
options.set("black")

color_dropdown = tkinter.OptionMenu(win, options, *colors)
tkinter.Label(win, text = "Select a color").grid(rows,cols)
color_dropdown.grid(rows, cols)

tkinter.mainloop()

#----------Mouse Tracing----------

#----------Pixels---------- (incomplete)

fill_in = win.getMouse()

square = Rectangle(Point(fill_in), Point(fill_in+50))
square.setFill(color_rgb(0,0,0))
square.draw(win)

#----------Save File----------

