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
    self.TITLE = "2D Game"
    self.AUTHOR = "3etamax"
    self.prefs = GamePreferencesIFace()
    self.date_started = None
    self.game_log = GameLog()
    self.DISPLAYSURF = pygame.display.set_mode((self.prefs.WINWIDTH, self.prefs.WINHEIGHT))


  def tick(self,game_data_object):
    pass

  def register_core(self,core_game_engine):
    self.core_game_eninge = core_game_engine
  
  def start(self):
    pygame.display.set_caption(self.title)
    #pygame.display.set_icon(pygame.image.load('gameicon.png'))

class GamePreferencesIFace(object):

  def __init__(self):
    self.FPS = 30 # frames per second to update the screen
    self.WINWIDTH = 800 # width of the program's window, in pixels
    self.WINHEIGHT = 600 # height in pixels
    self.HALF_WINWIDTH = int(self.WINWIDTH / 2)
    self.HALF_WINHEIGHT = int(self.WINHEIGHT / 2)
    self.DEBUG = True

class Level(object):
  
  def __init__(self, displaysurf, level_data = None, modifiers = None):
    self.level_data = level_data
    self.modifiers = modifiers
    self.displaysurf = displaysurf

  def load(self):
    self.displaysurf.fill((255, 0, 0))

class GameController(object):

  """
  
    Returns a reference to an object that maintains the state of all pressed keys - abstracts out gamepads. Currently calling this method on each frame, will probably want to revise that or optimize it.

    Think Jill Of The Jungle responsiveness. I may only want to sample input every 1/2 second

  CONTROLLER_STATE - Dict returned to GameState objects on each tick
  CONTROLLER_DIRECTION_CODES - Dict mapping Controller Input to the controller_state object

  """

  self.controller_direction_codes = {}
  self.controller_state = {
                                'LEFT':False,
                                'RIGHT':False,
                                'UP':False,
                                'DOWN':False,
                                'JUMP':False,
                                'START':False,
                                'RUN': False
                                'WEP_1': False,
                                'WEP_2': False,
                                'WEP_3': False,
                                'WEP_4': False,
                                'WEP_5': False,
                              }

  def __init__(self):
    self._read_controller_config()

  def _read_controller_config(self):
    # TODO: Read input state from config file
    controller_mapping = [
                            (97,'LEFT'),
                            (110,'RIGHT'),
                            (119,'UP'),
                            (115,'DOWN'),
                            (0,'JUMP'),
                            (2,'START'),
                            (3,'RUN'),
                            (4,'WEP_1'),
                            (5,'WEP_2'),
                            (6,'WEP_3'),
                            (7,'WEP_4'),
                            (8,'WEP_5')
    ]

    for control_key in controller_mapping:
      self.controller_direction_codes[control_key[0]] = control_key[1]

  def terminate(self):
    raise Exception('Quit called')

  def tick(self):
    for event in pygame.event.get([KEYUP,KEYDOWN]):
      if event.type == KEYDOWN: 
        self.controller_direction[event.key] = True
      elif: event.type == KEYUP:
        self.controller_direction[event.key] = False 
    
class Core(object):

  def __init__(self,debug=True):

    # GAME INIT
    self.clock = pygame.time.Clock()
    self.controller = GameController()
    self.sys_log = SysLog()

    # PYGAME INIT
    pygame.init()

  def register_game(self,game_data_object):
    self.game_data_object = game_data_object
    pygame.key.set_repeat(1,self.game_data_object.FPS)

  def start(self):
    self.game_data_object.start()

    while True:

      # Main loop
      #   1) Repaint display
      #   2) Update controller
      #   3) Update the game engine  - engine just polls internal ref for game controller state
      #   4) Tick the clock 

      pygame.display.update()
      self.controller.tick()
      self.game_data_object.tick(self.game_tick_data)
      self.clock.tick(self.game_data_object.FPS)
