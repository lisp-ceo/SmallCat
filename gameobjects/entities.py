"""
   Moveable game entities
"""

import sys, pygame
from vectors import Vector3
from pygame.locals import *

class GameEntity(object):

  def __init__(self, level, name, image):
    self.level = level
    self.name = name
    self.image = image
    self.location = Vector3(0,0,0)
    self.destination = Vector3(0,0,0)
    self.speed = 0

    self.brain = None

    self.id = 0

  def render(self, surface):
    x, y, z = self.location
    w, h = self.image.get_size()
    surface.blit(self.image, (x-w/2, y-h/2))

  def process(self, time_passed):
    self.brain.think()

class Player(object):
  
  def __init__(self,controller,x=0,y=0):
    # Bind controls
    # Player persists 
    # Set instance variables
    
    self.controller = controller
    self.LEFT = 'left';
    self.RIGHT = 'right';
    self.active = 1
    self.surface = pygame.transform.scale()
    self.facing = self.LEFT;
    self.x = x
    self.y = y
    self.lives = 5
    self.hp = 3
    pass

  def tick():
    pass

class GameEnemy(GameEntity):
  pass

class CheapGameEnemy(GameEnemy):
  pass

