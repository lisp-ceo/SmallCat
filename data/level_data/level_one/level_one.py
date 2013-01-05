"""

  Python-style block comment. Parser will ignore everything
  that is here.

"""
from ..level import LevelData, StageData
import random, sys, copy, os, pygame
from pygame.locals import *

class LevelOneData(LevelData):
  
  def __init__(self):
    super(LevelOneData,self).__init__()
    self.canvas_size = (60,20)
    self.BLOCKS = {
      '#' : pygame.image.load(os.path.join('data','level_data','level_one','dev_texture1.bmp')),
      ' ' : pygame.image.load(os.path.join('data','level_data','level_one','dev_texture2.bmp'))
    }
    self.BLOCKDATA = ['#',' ']
