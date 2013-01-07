"""
  Camera class determines the position and zoom of the camera

  TODO: Register preferences with this object correctly (gameeobjects.engine.GamePreferencesIFace
  
"""

import pygame

class Camera(object):
  def __init__(self):
    self.WINWIDTH = 800 # width of the program's window, in pixels
    self.WINHEIGHT = 600 # height in pixels
    self.ZOOM_BOUNDS = (0,100)
    self.current_zoom = 0 

  def calc_view(self):
    #if self.current_zoom < 100:
    #  self.current_zoom +=1
    #else:
    #  self.current_zoom = 1
    zoomed_w = (self.WINWIDTH - self.map_surface_dims[0]) * self.current_zoom/100 + self.map_surface_dims[0]
    zoomed_h = (self.WINHEIGHT - self.map_surface_dims[1]) * self.current_zoom/100 + self.map_surface_dims[1]

    return pygame.transform.scale(self.map_surface,(zoomed_w,zoomed_h))

  def register_map_surface(self,map_surface,map_surface_dims):
    self.map_surface = map_surface
    self.map_surface_dims = map_surface_dims
