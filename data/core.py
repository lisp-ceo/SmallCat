#from menu import 
from gameobjects.engine import GameDataIFace, GamePreferencesIFace
from game_states import Menu, CutScene, Level
import datetime

class Game(GameDataIFace):
  def __init__(self):
    GameDataIFace.__init__(self)
    self.FPS = 60
    self.title = "Small Cat"
    self.date_started = datetime.date(2013,1,5)
    self.GAME_STATES = {0:'MENU',1:'GAME',3:'CUTSCENE'}
    self.game_state_delegator = GameStateDelegator()

  def start(self):
    super(Game,self).start()
    self.current_state = self.GAME_STATES[0]
    self.game_state_delegator.new_state(

  def tick(self,game_data_object):
    super(Game,self).tick(game_data_object)
    self.state_function.tick(game_data_object)

    """

    Game Loop:
      * Move object on stage
      * Read game data object

    """

class GameStateDelegator(object):
  """
    Manages instantiating and deconstructing the game states
  """

  def __init__(self):
    self.GAME_STATES = {0:'MENU',1:'GAME',3:'CUTSCENE'}
    self.current_state


  def new_state(self, state):
    pass      
  
class GamePreferences(GamePreferencesIFace):
  def __init__(self):
    GamePreferencesIFace.__init__(self)
    self.game_log.write("Game Log Handled by subclass")
