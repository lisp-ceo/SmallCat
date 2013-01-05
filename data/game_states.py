"""

  Handles menus
    
  Sets options
  Loads games

"""

from tile_loader import TileLoader

class GameState(object):

  def __init__(self,game_ref,delegator_ref):
    self.INTERNAL_STATES = ["LOADING","ACTIVE","DECONSTRUCTING"]
    self.internal_state = 0
    self.delegator = delegator_ref
    self.game_ref = game_ref
    self.log = self.game_ref.game_log.write
    self.controller = self.game_ref.controller_settings['key_down_codes']
    self.canvas = self.game_ref.DISPLAYSURF
    self.load()

  def load(self): 
    # Call out to tile loader
    pass

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
    #if len(self.controller) != 0:
    #  self.log(self.controller)
    #self.canvas.fill((24, 255, 0))

    #if 49 in self.controller:
    #  self.delegator.next_state(self.GAME_STATE)
    self.delegator.next_state(self.GAME_STATE)

  def deconstruct(self):
    pass

class Level(GameState): 

  def __init__(self,game_ref,delegator_ref):
    super(Level,self).__init__(game_ref,delegator_ref)
    self.GAME_STATE = 1 # Refs to GAME_STATES in GameDataIFace
    self.load()

  def load(self):
    # Load Level data
    # Load Tile data
    # Load Images
    self.tile_loader = TileLoader()

  def tick(self,game_data_object): 
    if self.internal_state == 0:
      pass
    elif self.internal_state == 1:
      pass
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

