#!/usr/bin/env python

from gameobjects.engine import Core 
from data.core import Game

def main():
  core_game_engine = Core()
  game_data = Game()
  game_data.register_core(core_game_engine)
  core_game_engine.register_game(game_data)
  core_game_engine.start()

main()
