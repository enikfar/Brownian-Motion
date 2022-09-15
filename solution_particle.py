import random

class Particle:
  def __init__(self, x, y, color, tail_length):
    self.x = x
    self.y = y
    self.color = color
    self.tail_length = tail_length
    self.tail = []

  def get_color(self):
    return self.color

  def get_position(self):
    return (self.x, self.y)

  def get_tail(self):
    return self.tail

  def take_step(self, step,dim):
    if self.x > dim:
      self.x = 0
    if self.y > dim:
      self.y = 0  

    self.x += step 
    self.y += step
    if len(self.tail) > self.tail_length:
      del self.tail[0]
    self.tail.append((self.x, self.y))
