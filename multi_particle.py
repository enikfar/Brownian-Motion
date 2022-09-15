import picture
import random
import particle

def clear_frame(dim, bgnd):
  picture.set_fill_color(bgnd)
  picture.set_outline_color(bgnd)
  picture.draw_filled_square(0,0,dim)

def draw_particle(p):
  color = p.get_color()
  picture.set_fill_color(color)
  picture.set_outline_color(color)

  tail = p.get_tail()
  picture.draw_polyline(tail)

  (x,y) = p.get_position()
  picture.draw_filled_circle(x,y,5)

def main():
  dim = 400
  n_particles = 10
  n_steps = 100000000000000000
  step = 10
  tail_length = 50
  fgnds = ["pink", "lime", "coral", "skyblue"]
  bgnd = "black"

  picture.new_picture(dim,dim)

  x = dim//2
  y = dim//2

  # create particles
  particles = []
  for i in range(n_particles):
    p = particle.Particle(x, y, fgnds[i%len(fgnds)], tail_length)
    particles.append(p)

  # take steps
  for i in range(n_steps):
    clear_frame(dim, bgnd)
    for p in particles:
      p.take_step(step)
      draw_particle(p)

    picture.display()

  picture.run()


main()
