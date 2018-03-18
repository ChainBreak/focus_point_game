#!/usr/bin/env python

from game_engine import GameEngine
import threading

class GameManager():
    def __init__(self):
        self.game_dict = {}
        self.lock = threading.Lock()

    def get_or_add_game(self,game_name):
        with self.lock:
            if not game_name in self.game_dict:
                self.game_dict[game_name] = GameEngine(game_name)
            return self.game_dict[game_name]
