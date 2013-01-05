"""
  Parent class for all Level and Stage objects
"""

class LevelData(object):

  """
    Vars

    # - Impassible 
    ' ' - Generic 
    $ - Hiding spot

  """
  
  def __init__(self):
    self.stages = []
    self.CANVAS_MAX_H = 600
    self.CANVAS_MAX_W = 800
    self.CANVAS_MIN_H = 20
    self.CANVAS_MIN_W = 20
    self.BLOCKS_MAX_H = 20
    self.BLOCKS_MAX_W = 20
    self.BLOCKS_MIN_H = 20
    self.BLOCKS_MIN_W = 20

    self.canvas_size = None
    self.BLOCKS = {} # Dictionary of images used as tiles
    self.BLOCKDATA = [] # Array of character codes representing the blocks
    self.MAPPING = {
      'IMPASSIBLE':'#',
      'GENERIC':' ',
      'IMPASSIBLE':'$',
      'BIGTESTICLES' :'@'
    } # Dictionary that maps file data to images
    self.canvas = None # This attribute is filled in by the caller

class StageData(object):
  pass
