"""

  Handles menus
    
  Sets options
  Loads games

"""

class GameState(object):

  def __init__(self,game_ref):
    self.is_loading = True
    self.game_ref = game_ref

  def load(self): pass

  def tick(self): pass

class Menu(GameState):

  def __init__(self,game_ref):
    super(Menu,self).__init__(game_ref)

  def tick(self,game_data_object): 
    print self.game_ref.controller_settings['key_down_codes']
    pass

  def deconstruct(self):
    pass

class CutScene(GameState): pass

class Level(GameState): pass
