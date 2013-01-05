"""
  Logs split out and subclassed to facilitate named objects for ease of development.
  The criticism that this is superfluous is not valid as the naming is important.
"""

class Log(object):
  @classmethod
  def write(self, console_text):
    print console_text

class SysLog(Log):
  """
    Log used By Gameobjects.engine.Core
  """
  def __init__(self):
    self.write("Sys Log initialized")

class GameLog(Log):
  """
    Log used by clients implementing gameobjects.engine.GamePreferencesIFace 
  """
  def __init__(self):
    self.write("Game Log initialized")
