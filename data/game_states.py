"""

  Handles menus
    
  Sets options
  Loads games


  TODO: Utilize multi-threading in Python to correctly async load levels

"""

from tile_loader import TileLoader
from camera import Camera

class GameState(object):

  def __init__(self,game_ref,delegator_ref):
    self.INTERNAL_STATES = ["LOADING","ACTIVE","DECONSTRUCTING"]
    self.internal_state = 0
    self.delegator = delegator_ref
    self.game_ref = game_ref
    self.log = self.game_ref.game_log.write
    self.controller = self.game_ref.controller_settings['key_down_codes']
    self.canvas = self.game_ref.DISPLAYSURF

  def tick(self,game_data_object): 
    pass

  def deconstruct(self): 
    del self

  def set_internal_state(self,state):
    self.internal_state = state

class Menu(GameState):

  def __init__(self,game_ref,delegator_ref):
    super(Menu,self).__init__(game_ref,delegator_ref)
    self.GAME_STATE = 0 # Refs to GAME_STATES in GameDataIFace
    #self.log("Press 1 to enter color switch mode ")

  def tick(self,game_data_object): 
    if len(self.controller) != 0:
      self.log(self.controller)
    self.canvas.fill((255, 0, 0))

    if 49 in self.controller:
      self.delegator.next_state(self.GAME_STATE)

  def deconstruct(self):
    pass

class Level(GameState): 
  def __init__(self,game_ref,delegator_ref):
    super(Level,self).__init__(game_ref,delegator_ref)
    self.camera = Camera()
    self.GAME_STATE = 1 # Refs to GAME_STATES in GameDataIFace
    self.level_to_load = 1
    self.load(1)

  def load(self,level_to_load):
    self.tile_loader = TileLoader(level_to_load) # Returns a reference to a display surface
    self.set_internal_state(1) # Level has finished loading
    self.camera.register_map_surface(self.tile_loader.get_map_surface(),self.tile_loader.get_map_surface_dims())

  def tick(self,game_data_object): 
    self.canvas.fill((0, 255, 0))
    if self.internal_state == 0:
      self.canvas.fill((0, 255, 0))
    elif self.internal_state == 1:
      self.canvas.fill((0, 0, 255))
      self.canvas.blit(self.camera.calc_view(),(0,0))
    elif self.internal_state == 2:
      pass
    else:
      raise Exception("Unhandled internal_state")


class CutScene(GameState): 

  def __init__(self,game_ref,delegator_ref):
    super(CutScene,self).__init__(game_ref,delegator_ref)
    self.GAME_STATE = 2 # Refs to GAME_STATES in GameDataIFace

  def tick(self,game_data_object): 
    self.log(self.controller)
    self.canvas.fill((254, 5, 10))

