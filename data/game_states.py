"""

  Handles menus
    
  Sets options
  Loads games

"""

class GameState(object):

  def __init__(self):
    self.is_loading = True

  def load(self): pass

class Menu(GameState):

  def __init__(self): pass

  def tick(self,game_data_object): pass

  def deconstruct(self):

class CutScene(GameState): pass

class Level(GameState): pass
