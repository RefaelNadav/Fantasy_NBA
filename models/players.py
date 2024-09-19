
from db import db



class PlayerStats(db.Model):  # Inherit from db.Model
    _tablename_ = 'player_stats'


    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(30), nullable=True)
    position = db.Column(db.String(30), nullable=True)
    games = db.Column(db.Integer, nullable=True)
    field_goals = db.Column(db.Integer, nullable=True)
    three_percent = db.Column(db.Float, nullable=True)
    two_percent = db.Column(db.Float, nullable=True)
    assists = db.Column(db.Integer, nullable=True)
    turnovers = db.Column(db.Integer, nullable=True)
    points = db.Column(db.Integer, nullable=True)
    team = db.Column(db.String(10), nullable=True)
    season = db.Column(db.Integer, nullable=True)
    player_id = db.Column(db.String(10), nullable=True)
    ATR = db.Column(db.Float, nullable=True)
    PPG_ratio = db.Column(db.Float, nullable=True)

    def _repr_(self):
        return (f"<PlayerStats(player_name={self.player_name}, team={self.team},"
                f" season={self.season})>")

    def to_dict(self):
        return {
            'id': self.id,
            'player_name': self.player_name,
            'position': self.position,
            'games': self.games,
            'field_goals': self.field_goals,
            'three_percent': self.three_percent,
            'two_percent': self.two_percent,
            'assists': self.assists,
            'turnovers': self.turnovers,
            'points': self.points,
            'team': self.team,
            'season': self.season,
            'player_id': self.player_id,
            'ATR': self.ATR,
            'PPG_ratio': self.PPG_ratio
        }



