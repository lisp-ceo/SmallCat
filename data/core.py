from gameobjects.engine import GameDataIFace, GamePreferencesIFace

class Game(GameDataIFace):
  def __init__(self):
    GameDataIFace.__init__(self)
    #super(GameDataIFace,self).__init__()
    self.FPS = 60
    print "Game"

class GamePreferences(GamePreferencesIFace):
  def __init__(self):
    pass
