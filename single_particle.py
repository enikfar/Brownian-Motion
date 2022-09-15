import picture
import random

def clear_frame(dim, bgnd):
  picture.set_fill_color(bgnd)
  picture.set_outline_color(bgnd)
  picture.draw_filled_square(0,0,dim)

def take_step(x,y,step,dim):
  if x > dim:
     x = 0
  if y > dim:
     y = 0  

  x += step 
  y += step
  return (x,y)

def draw_particle(x,y,tail,color,dim):
  picture.set_fill_color(color)
  picture.set_outline_color(color)
  picture.draw_polyline(tail)
  if x > dim:
    x = 0
  if y > dim:
    y = 0  
  picture.draw_filled_circle(x,y,5)

def main():
  dim = 400
  n_steps = 1000
  step = 3
  tail_length = 30
  fgnd = "white"
  bgnd = "black"

  picture.new_picture(dim,dim)

  x = dim//2
  y = dim//2
  tail = []

  for i in range(n_steps):
    clear_frame(dim, bgnd)
    (x,y) = take_step(x,y,step,dim)
    if x > dim:
      tail = []
    if y > dim:
      tail = []  
    if len(tail) > tail_length:
      del tail[0]
    tail.append((x,y))
    draw_particle(x,y,tail,fgnd,dim)
    picture.display()

  picture.run()


main()
