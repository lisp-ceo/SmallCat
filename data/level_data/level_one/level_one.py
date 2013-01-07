"""

  Python-style block comment. Parser will ignore everything
  that is here.


  TODO: Re-work if(1) to support multiple dev environments


  BLOCKS - A dictionary of tuples mapping symbols in BLOCKDATA to canvas objects:
           0 - Canvas objects
           1 - Their dimensions 
  BLOCKDATA - A list of representing the map to display

"""
from ..level import LevelData, StageData
import random, sys, copy, os, pygame
from pygame.locals import *

class LevelOneData(LevelData):
  
  def __init__(self):
    super(LevelOneData,self).__init__()
    self.block_size = (800,450)
    if 1:
      self.BLOCKS = {
        '1' : (pygame.image.load(os.path.join('data','level_data','common','Tile_Dev_1.png')),(800,450)),
        '2' : (pygame.image.load(os.path.join('data','level_data','common','Tile_Dev_2.png')),(800,450)),
        '3' : (pygame.image.load(os.path.join('data','level_data','common','Tile_Dev_3.png')),(800,450)),
        '4' : (pygame.image.load(os.path.join('data','level_data','common','Tile_Dev_4.png')),(800,450)),
        '5' : (pygame.image.load(os.path.join('data','level_data','common','Tile_Dev_5.png')),(800,450)),
        '6' : (pygame.image.load(os.path.join('data','level_data','common','Tile_Dev_6.png')),(800,450))
      }
      self.BLOCKDATA = [
                         ['6','5','4','3','2','1'],
                         ['1','2','3','4','5','6'],
                         ['6','5','4','3','2','1'],
                         ['1','2','3','4','5','6'],
      ]
      self.canvas_size = (self.block_size[0] * len(self.BLOCKDATA[0]), self.block_size[1] * len(self.block_size)) # Assumes equal-sized sub-arrays


    else:
      self.canvas_size = (80,80)
      self.BLOCKS = {
        '#' : pygame.image.load(os.path.join('data','level_data','level_one','dev_texture1.bmp')),
        ' ' : pygame.image.load(os.path.join('data','level_data','level_one','dev_texture2.bmp'))
      }
      self.BLOCKDATA = [
                         [' ',' ',' ',' '],
                         [' ','#','#',' '],
                         [' ','#','#',' '],
                         [' ',' ',' ',' ']
      ]
