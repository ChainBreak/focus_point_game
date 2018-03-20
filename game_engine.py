#!/usr/bin/env python

from player import Player
import json
import uuid
class GameEngine():

    def __init__(self,name):
        self.name = name
        self.player_dict = {}
        self.player_counter = 0

    def get_or_add_player(self,player_id):

        if not player_id in self.player_dict:
            self.player_counter += 1
            player_id = str(uuid.uuid4())
            player_name = "Player %i" % self.player_counter
            self.player_dict[player_id] = Player(player_id,player_name)

        return self.player_dict[player_id]

    def try_get_player(self,player_id):
        return self.player_dict.get(player_id,None)

    def create_state_json(self,player_id):
        player = self.try_get_player(player_id)
        if player:
            state_json = {"ok": True,
                                    "player_name": player.name}
        else:
            state_json = {"state": {"ok": False}}

        return json.dumps(state_json)

    def process_player_data(self,player_id,player_data_dict):
        player = self.try_get_player(player_id)

        if player:
            if "player_name" in player_data_dict:
                player.name = player_data_dict["player_name"]
