#!/usr/bin/env python

class Player():

    def __init__(self,player_id,player_name):
        self.id = player_id
        self.name = player_name

    def __str__(self):
        return self.name
