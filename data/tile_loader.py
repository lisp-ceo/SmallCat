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

  def get_map_surface_dims(self):
    return self.tile_parser.canvas_data.map_surface_dims # Returns a surface object that's blitted every second

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
    self.canvas_data.map_surface_dims = self.canvas_data.canvas_size
    self.canvas_data.map_surface = pygame.Surface((self.canvas_data.canvas_size)) # Creates new surface object
    blit_target = (0,0) 
    blit_size = {'w':20,'h':20} # TODO: Associate this with block
    for level in self.canvas_data.BLOCKDATA:
      for block in level:
        blit_size = {'w':self.canvas_data.BLOCKS[block][1][0],'h':self.canvas_data.BLOCKS[block][1][1]} # TODO: Make sure this works with differently sized blocks - will not mesh well
        self.canvas_data.map_surface.blit(self.canvas_data.BLOCKS[block][0],blit_target)
        blit_target = (blit_target[0]+blit_size['w'],blit_target[1])
      blit_target = (0,blit_target[1]+blit_size['h'])
