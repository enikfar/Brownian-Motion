import random

class Particle:
  def __init__(self, x, y, color, tail_length):
    self.x = x
    self.y = y
    self.color = color
    self.tail_length = tail_length
    self.tail = []

  def take_step(self, step):
    # update current position
    self.x += random.randrange(-step,step+1)
    self.y += random.randrange(-step,step+1)

    # adding position to tail
    if len(self.tail) > self.tail_length:
      del self.tail[0]
    
    self.tail.append((self.x, self.y))

  def get_color(self):
    return self.color

  def get_position(self):
    return (self.x, self.y)

  def get_tail(self):
    return self.tail
