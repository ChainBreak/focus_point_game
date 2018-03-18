#!/usr/bin/env python

from flask import Flask, render_template, request, make_response, url_for
from game_manager import GameManager


app = Flask(__name__)

global game_manager
game_manager = GameManager()

@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/play/<game_name>/')
def game(game_name = None):
    global game_manager

    game = game_manager.get_or_add_game(game_name)
    cookie_game_name = request.cookies.get('game_name')

    if cookie_game_name == game_name:
        player_id = request.cookies.get('player_id')
    else:
        player_id = None

    player = game.get_or_add_player(player_id)
    print(player)
    response = make_response( render_template('game.html'))
    response.set_cookie("player_id",str(player.id))
    response.set_cookie("game_name",game_name)

    return response


@app.route("/play/<game_name>/game_state.json")
def game_state(game_name = None):
    global game_manager

    game = game_manager.get_or_add_game(game_name)
    player_id = request.cookies.get('player_id')
    player = game.get_or_add_player(player_id)

    response = make_response( game.create_state_json(player_id))
    response.set_cookie("player_id",str(player.id))
    response.set_cookie("game_name",game_name)

    return response




if __name__ == "__main__":
    app.run('0.0.0.0',80,threaded=True)
