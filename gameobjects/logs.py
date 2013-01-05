"""
  Logs split out and subclassed to facilitate named objects for ease of development.
  The criticism that this is superfluous is not valid as the naming is important.
"""

class Log(object):

  def __init__(self):
    self.log_type = "Log"

  # @classmethod - Uncommenting this will produce strange errors - probably something to do with
  #                calling a static method dynamically

  def write(self, console_text):
    print self.log_type + ': ' +str(console_text)

class SysLog(Log):
  """
    Log used By Gameobjects.engine.Core
  """
  def __init__(self):
    self.log_type = "SysLog"
    self.write("Sys Log initialized")

class GameLog(Log):
  """
    Log used by clients implementing gameobjects.engine.GamePreferencesIFace 
  """
  def __init__(self):
    self.log_type = "GameLog"
    self.write("Game Log initialized")
