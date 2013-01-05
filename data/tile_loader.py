import pygame
from level_data.level_one.level_one import LevelOneData

"""

  Tile-base map loading

"""

class TileLoader(object):
  """
    Returns a list that the parent class knows how to render
  """
  
  def __init__(self,level_to_load):
    self.LEVELS = {
      1:LevelOneData
    }
    self.level_to_load = level_to_load
    self.tile_parser = TileParser(self.LEVELS[level_to_load])

  def get_map_surface(self):
    return self.tile_parser.canvas_data.map_surface # Returns a surface object that's blitted every second

class TileParser(object):
  """
    Parses tile objects - returns a Canvas object
  """

  def __init__(self,level_to_load):
    self.canvas_data = level_to_load()
    self.parse_canvas_data(self.canvas_data)
    
  def parse_canvas_data(self,level_data_obj):
    self.canvas_data.map_surface = pygame.Surface((self.canvas_data.canvas_size)) # Creates new surface object
    blit_target = (0,0) 
    blit_size = {'w':20,'y':20}
    for block in self.canvas_data.BLOCKDATA:
      self.canvas_data.map_surface.blit(self.canvas_data.BLOCKS[block],blit_target)
      blit_target = (blit_target[0]+blit_size['w'],0)
