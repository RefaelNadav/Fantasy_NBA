
from flask import Flask, jsonify
from db import db
from blue_print.players import players_bp
# from services.request_api import get_players_by_season


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(players_bp)

# years = [2022, 2023, 2024]
# @app.route('/')
# def home():
#     try:
#         for year in years:
#             get_players_by_season(year)
#         return jsonify({'message': 'Database created successfully!'}), 200
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/')
# def home():
#     try:





if __name__ == "__main__":

    app.run(debug=True)
