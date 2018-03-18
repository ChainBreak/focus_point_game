#!/usr/bin/env python

from player import Player
import json

class GameEngine():

    def __init__(self,name):
        self.name = name
        self.player_dict = {}
        self.id_counter = 0

    def get_or_add_player(self,player_id):
        if not player_id is None:
            player_id = int(player_id)

        if not player_id in self.player_dict:
            player_id = self.get_unique_player_id()
            self.player_dict[player_id] = Player(player_id)

        return self.player_dict[player_id]

    def get_unique_player_id(self):
        self.id_counter += 1
        return  self.id_counter

    def get_game_and_player(self,game_name,player_id):
        pass

    def create_state_json(self,player_id):
        player = self.get_or_add_player(player_id)
        state_json = {"state": {"player_name": player.name}}

        return json.dumps(state_json)
