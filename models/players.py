
from db import db



class PlayerStats(db.Model):  # Inherit from db.Model
    _tablename_ = 'player_stats'


    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(30), nullable=False)
    position = db.Column(db.String(30), nullable=False)
    games = db.Column(db.Integer, nullable=False)
    field_goals = db.Column(db.Integer, nullable=True)
    three_percent = db.Column(db.Float, nullable=True)
    two_percent = db.Column(db.Float, nullable=False)
    assists = db.Column(db.Integer, nullable=True)
    turnovers = db.Column(db.Integer, nullable=True)
    points = db.Column(db.Integer, nullable=True)
    team = db.Column(db.String(10), nullable=False)
    season = db.Column(db.Integer, nullable=False)
    player_id = db.Column(db.String(10), nullable=False)
    ATR = db.Column(db.Float, nullable=True)
    PPG_ratio = db.Column(db.Float, nullable=True)

    def _repr_(self):
        return (f"<PlayerStats(player_name={self.player_name}, team={self.team},"
                f" season={self.season})>")



if __name__ == "_main_":
    db.create_all()

    # Add a sample player (like Jalen Crutcher)
    player = PlayerStats(id=18127, player_name="Jalen Crutcher", position="PG", games=1, field_goals=0,
                         three_percent=None, two_percent=0.000, assists=0, turnovers=0,
                         points=0, team="NOP", season=2024, player_id="crutcja01")

    db.session.add(player)
    db.session.commit()