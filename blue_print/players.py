from flask import Blueprint, request, jsonify
from models.players import PlayerStats
from services.get_players import get_players_by_position




players_bp = Blueprint('players', __name__, url_prefix='/api/players')



# @players_bp.route('/', methods=['GET'])
# def get_players():
#     players = PlayerStats.query.all()
#     return jsonify([player.to_dict() for player in players]), 200

@players_bp.route('/', methods=['GET'])
def get_players():
    position = request.args.get('position')

    if not position:
        return jsonify({"error": "Position is required"}), 400
    players = get_players_by_position(position)
    return players
    # return jsonify([player.to_dict() for player in players]), 200


# def get_users():
#     identity = get_jwt_identity()
#     if identity == 'admin1':
#         print(identity)
#         users = User.query.all()
#         users_response = generate_users_response(users=users)
#         return jsonify(users_response), 200