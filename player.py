#!/usr/bin/env python

class Player():

    def __init__(self,player_id):
        self.id = player_id
        self.name = "Player %i" % player_id

    def __str__(self):
        return str(self.id)
