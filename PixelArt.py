# Pixel Art Program
# Create simple pixel art

# Made by Naomi Lewis through Python 3.7.4

import graphics
from graphics import *

def main():
  
#----------Parameters----------

  canvas_width = 512
  canvas_height = 512

  tool_width = 200

  margin = 32

  rows, cols = 16, 16

  wid = margin + canvas_width + margin + tool_width + margin
  hei = 2 * margin + canvas_height

#----------Start Screen----------

  win = GraphWin("PixelArt", wid, hei)
  win.setBackground(color_rgb(255, 255, 255))

  txt, box = makebutton("Click here to start drawing",
                        wid / 2, hei / 2, 250, 50, [0, 0, 0])
  txt._reconfig('font', ('Manaspace Regular', 18))
  txt.setTextColor(color_rgb(250, 250, 250))
  
  box.draw(win)
  txt.draw(win)

  win.getMouse()
  # Add restrictions

#----------Undraw the button----------

  txt.undraw()
  box.undraw()

#----------Grid----------

  drawgrid(win, margin, canvas_width, canvas_height, rows,
           cols, 240, 240, 240)

#----------Coloring----------

  color_choice(win, canvas_width, margin, 255, 127, 80)

#------User Interaction-------

  while True:
    # Wait for user to click somewhere

    pt = win.checkMouse()
    if pt:
      if clicked_on_canvas(pt, margin, canvas_width, canvas_height):
        row, col = where_did_i_click(pt, margin, canvas_width, canvas_height, rows, cols)
        print("Let's paint cell ({}, {})!".format(row, col))

        paint(win, margin, canvas_width, canvas_height, rows, cols, row,
              col, 'blue', color_rgb(240, 240, 240))
      else:
        print("Hey! You clicked on ({}, {})".format(pt.getX(), pt.getY()))

    key = win.checkKey()
    if key:
      if key == "Escape":
        win.close()
      else:
        print("Hey! You pressed", key)

#----------Save File----------



#----------Functions----------

def clicked_on_canvas(pt, margin, wid, hei):
  ''' Return true if the user clicked on the canvas, false otherwise.'''
  x = pt.getX()
  y = pt.getY()

  return (x >= margin and x <= margin + wid) and (y >= margin and y <= margin + hei)

#-----------------------------

def color_choice(win, canvas_width, margin, r, g, b):
  '''Select a color using its RGB value'''

  color_text = Text(Point(margin + margin + canvas_width + 100, 54), "RGB Color")
  color_text._reconfig('font', ('Manaspace Regular', 14))
  color_text.setTextColor(color_rgb(0, 0, 0))
  
  color_box = Rectangle(Point(margin + margin + canvas_width, 64),
                        Point(margin + margin + canvas_width + 200, 96))
  color_box.setFill(color_rgb(r, g, b))
  color_box.setOutline(color_rgb(r, g, b))

  color_entry = Entry(Point(margin + margin + canvas_width + 100, 80), 12)
  color_entry.setText("0,0,255")
  color_entry.setFill(color_rgb(250, 250, 250))

  #color_input = int(input(color_entry.getText()))

  #R, G, B = float(color_input.split(','))

  color_text.draw(win)
  color_box.draw(win)
  color_entry.draw(win)

  #return R, G, B

#-----------------------------

def drawgrid(win, margin, canvas_width, canvas_height, rows, cols, r, g, b):
  '''Draw a grid with lines of color (r,g,b).'''

  #Background color
  

  # Box filled white
  box = Rectangle(Point(margin, margin),
                  Point(margin + canvas_width, margin + canvas_height))
  box.setFill(color_rgb(255, 255, 255))
  box.setOutline(color_rgb(255, 255, 255))
  
  # Draw vertical lines
  pixels_per_cell = canvas_width / cols
  x = margin + pixels_per_cell
  for i in range(1, cols):
    vline = Line(Point(x, margin), Point(x, margin + canvas_height))
    vline.setWidth(1 / 5)
    vline.setOutline(color_rgb(r, g, b))
    vline.draw(win)
    x += pixels_per_cell

  # Draw horizontal lines
  pixels_per_cell = canvas_height / rows
  y = margin + pixels_per_cell
  for i in range(1, rows):
    hline = Line(Point(margin, y), Point(margin + canvas_width, y))
    hline.setWidth(1 / 5)
    hline.setOutline(color_rgb(r, g, b))
    hline.draw(win)
    y += pixels_per_cell

  # Draw outer box
  outer_box = Rectangle(Point(margin, margin),
                  Point(margin + canvas_width, margin + canvas_height))
  outer_box.draw(win)
  

#-----------------------------

def makebutton(txt, x, y, w, h, clr):
  '''Make a button with the given text.'''
  txt = Text(Point(x, y), txt)
  box = Rectangle(Point(x - w, y - h ), Point(x + w, y + h ))
  box.setFill(color_rgb(clr[0], clr[1], clr[2]))

  return txt, box

#-----------------------------

def paint(win, margin, wid, hei, rows, cols, row, col, clr, gridclr):
  '''Paint a cell in the canvas.'''
  ppx, ppy = wid / cols, hei / rows
  x0 = margin + (col - 1) * ppx
  y0 = margin + (row - 1) * ppy
  x1 = x0 + ppx
  y1 = y0 + ppy
  rect = Rectangle(Point(x0, y0), Point(x1, y1))
  rect.setOutline(gridclr)
  rect.setFill(clr)
  rect.draw(win)

#-----------------------------

def where_did_i_click(pt, margin, wid, hei, rows, cols):
  ''' Return row and column in the canvas where the user clicked.'''
  x = pt.getX() - margin
  y = pt.getY() - margin

  ppx = wid / cols  # pixels per cell in x direction
  ppy = hei / rows  # pixels per cell in y direction

  row = int((y // ppy) + 1)
  col = int((x // ppx) + 1)

  return row, col


if __name__ == "__main__":
  main()
