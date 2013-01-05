"""
   Data structures that comprise the game engine
"""

import pygame
from logs import GameLog, SysLog

class GameDataIFace(object):
  def __init__(self):
    self.title = "2D Game"
    self.author = "James Rhys"
    self.prefs = GamePreferencesIFace()
    self.date_started = None
    self.game_log = GameLog()
    self.game_log.write("Game Log initialized")

  def tick(self):
    pass

  def register_core(self,core_game_engine):
    self.core_game_eninge = core_game_engine
  
  def start(self):
    # Custom error if not overridden
    pass

class GamePreferencesIFace(object):

  def __init__(self):
    self.FPS = 30 # frames per second to update the screen
    self.WINWIDTH = 800 # width of the program's window, in pixels
    self.WINHEIGHT = 600 # height in pixels
    self.HALF_WINWIDTH = int(self.WINWIDTH / 2)
    self.HALF_WINHEIGHT = int(self.WINHEIGHT / 2)
    self.DEBUG = True
    self.DISPLAYSURF = None

# def register_game(self, game_data):
#   self.game_data = game_data

class Level(object):
  
  def __init__(self, displaysurf, level_data = None, modifiers = None):
    self.level_data = level_data
    self.modifiers = modifiers
    self.displaysurf = displaysurf

  def load(self):
    self.displaysurf.fill((255, 0, 0))

class GameController(object):

  def terminate(self):
    raise Exception('Quit called')

  def tick(self):
    for event in pygame.event.get():
      if event.type == QUIT:
        self.terminate()
      elif event.type == KEYDOWN:
        if event.key in (K_UP, K_w):
          print "UP"
        elif event.key in (K_DOWN, K_s):
          print "DOWN"
        elif event.key in (K_LEFT, K_a):
          print "DOWN"
        elif event.key in (K_RIGHT, K_d):
          print "RIGHT"
        elif event.key == K_ESCAPE:
          print event.key
          self.terminate()
      elif event.type == KEYUP:
        if event.key in (K_LEFT, K_a):
          print event.key
        elif event.key in (K_RIGHT, K_d):
          print event.key
        elif event.key in (K_UP, K_w):
          print event.key
        elif event.key in (K_DOWN, K_s):
          print event.key
        elif event.key == K_ESCAPE:
          print event.key
          self.terminate()
    
class Core(object):

  def __init__(self,debug=True):

    # GAME INIT
    self.clock = pygame.time.Clock()
    self.controller = GameController()
    self.sys_log = SysLog

    # PYGAME INIT
    pygame.init()
    #self.prefs.DISPLAYSURF = pygame.display.set_mode((self.prefs.WINWIDTH, self.prefs.WINHEIGHT))

    #pygame.display.set_caption('2dgame. Debug: '+str(self.prefs.DEBUG))

#    self.level = Level(self.prefs.DISPLAYSURF)
#    self.level.load()

  def register_game(self,game_data_object):
    self.game_data_object = game_data_object

  def start(self):
    self.game_data_object.start()

    while True:
      #pygame.display.update()
      #self.controller.tick()
      self.clock.tick(self.game_data_object.FPS)
      self.game_data_object.tick() # Pass the engine all it needs to 
