from gameobjects.engine import GameDataIFace, GamePreferencesIFace
import datetime

class Game(GameDataIFace):
  def __init__(self):
    GameDataIFace.__init__(self)
    self.FPS = 60
    self.title = "Small Cat"
    self.date_started = datetime.date(2013,1,5)

  def tick(self,game_data_object):
   super(Game,self).tick(game_data_object)
   if game_data_object['controller'] is not None:
    print self.controller_settings

class GamePreferences(GamePreferencesIFace):
  def __init__(self):
    GamePreferencesIFace.__init__(self)
    self.game_log.write("Game Log Handled by subclass")
