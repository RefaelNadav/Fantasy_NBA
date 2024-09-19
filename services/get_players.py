from db import db
from models.players import PlayerStats
from flask import jsonify
def get_players_by_position(position):
    players = PlayerStats.query.filter_by(position=position)
    # lst_players = [player.to_dict() for player in players]
    # dct_unique_players = {}
    # for player in lst_players:

    return jsonify([player.to_dict() for player in players]), 200