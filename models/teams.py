
from db import db

class Team(db.Model):  # Inherit from db.Model
    _tablename_ = 'teams'


    id = db.Column(db.Integer, primary_key=True)
    player_1 = db.Column(db.String(10), nullable=False)
    player_2 = db.Column(db.String(10), nullable=False)
    player_3 = db.Column(db.String(10), nullable=False)
    player_4 = db.Column(db.String(10), nullable=False)
    player_5 = db.Column(db.String(10), nullable=False)
