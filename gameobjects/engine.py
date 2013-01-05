"""
   Data structures that comprise the game engine

   TODO: Migrate pygame.key.set_repeat to somewhere better
   TODO: Refactor controller input handling to not bug out when non-input keys are input and outpu
   TODO: Correctly handle the keyboard state on each frame without spazzing the memory. Consider
   TODO: Replace shift functionality with calls to pygame.key.get_mods() and use bit-shifting 
   TODO: Refactor controller input handling to support gamepads
  
"""

import pygame
from pygame.locals import *
from logs import GameLog, SysLog

class GameDataIFace(object):
  def __init__(self):
    self.title = "2D Game"
    self.author = "James Rhys"
    self.prefs = GamePreferencesIFace()
    self.date_started = None
    self.game_log = GameLog()

    self.controller_direction_codes = ['LEFT','RIGHT','UP','DOWN',
                                  'UL','UR','DL','DR']
    self.controller_directions = {
                                  'LEFT':(97),
                                  'RIGHT':(110),
                                  'UP':(119),
                                  'DOWN':(115),
                                  'UL':(97,119),
                                  'UR':(110,119),
                                  'DL':(97,115),
                                  'DR':(110,115),
                                }
    self.controller_settings = {
      'key_down': False,
      'key_down_codes': [],
      'is_shift':False,
      'current_direction': None
    }

  def _update_controller_settings(self,game_data_object):
    
    if game_data_object['controller'] is not None:
      if game_data_object['controller'][0] == 2 and game_data_object['controller'][1] not in self.controller_settings['key_down_codes']: # KEY DOWN
        self.controller_settings['key_down'] += 1 
        self.controller_settings['key_down_codes'].append(game_data_object['controller'][1])
        if game_data_object['controller'][1] == 303 \
        or game_data_object['controller'][1] == 304:
          self.controller_settings['is_shift'] = True
      if game_data_object['controller'][0] == 3 and game_data_object['controller'][1] in self.controller_settings['key_down_codes']: # KEY UP
        self.controller_settings['key_down'] -= 1 
        self.controller_settings['key_down_codes'].remove(game_data_object['controller'][1])
        if game_data_object['controller'][1] == 303 \
        or game_data_object['controller'][1] == 304:
          self.controller_settings['is_shift'] = False 
      else:                                      #IGNORE FOR NOW 
        pass
      self._update_controller_direction()

  def _update_controller_direction(self):
    #for key in self.controller_settings['key_down_codes']
    pass

  def tick(self,game_data_object):
    """

      Does the following:
        - Updates the controller_settings object

    """
    self._update_controller_settings(game_data_object)

  def register_core(self,core_game_engine):
    self.core_game_eninge = core_game_engine
  
  def start(self):
    pygame.display.set_caption(self.title)

class GamePreferencesIFace(object):

  def __init__(self):
    self.FPS = 30 # frames per second to update the screen
    self.WINWIDTH = 800 # width of the program's window, in pixels
    self.WINHEIGHT = 600 # height in pixels
    self.HALF_WINWIDTH = int(self.WINWIDTH / 2)
    self.HALF_WINHEIGHT = int(self.WINHEIGHT / 2)
    self.DEBUG = True
    self.DISPLAYSURF = pygame.display.set_mode((self.WINWIDTH, self.WINHEIGHT))

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
    for event in pygame.event.get([KEYUP,KEYDOWN]):
      if event.type == KEYDOWN or event.type == KEYUP:
        return (event.type,event.key)
      #elif event.type == KEYDOWN:
      #  if event.key in (K_UP, K_w):
      #    print "UP"
      #  elif event.key in (K_DOWN, K_s):
      #    print "DOWN"
      #  elif event.key in (K_LEFT, K_a):
      #    print "DOWN"
      #  elif event.key in (K_RIGHT, K_d):
      #    print "RIGHT"
      #  elif event.key == K_ESCAPE:
      #    print event.key
      #    self.terminate()
      #elif event.type == KEYUP:
      #  if event.key in (K_LEFT, K_a):
      #    print event.key
      #  elif event.key in (K_RIGHT, K_d):
      #    print event.key
      #  elif event.key in (K_UP, K_w):
      #    print event.key
      #  elif event.key in (K_DOWN, K_s):
      #    print event.key
      #  elif event.key == K_ESCAPE:
      #    print event.key
      #    self.terminate()
    
class Core(object):

  def __init__(self,debug=True):

    # GAME INIT
    self.clock = pygame.time.Clock()
    self.controller = GameController()
    self.sys_log = SysLog()
    self.game_tick_data = {
      "controller" : None, 
    }

    # PYGAME INIT
    pygame.init()
    pygame.key.set_repeat(1,60)
  def register_game(self,game_data_object):
    self.game_data_object = game_data_object

  def start(self):
    self.game_data_object.start()

    while True:
      #pygame.display.update()
      self.game_tick_data['controller'] = self.controller.tick()
      self.game_data_object.tick(self.game_tick_data)
      self.clock.tick(self.game_data_object.FPS)
