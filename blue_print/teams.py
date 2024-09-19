
from flask import Blueprint, request, jsonify

teams_bp = Blueprint('teams', __name__, url_prefix='/api/teams')

# @teams_bp.route('/', methods=['POST'])
# def get_players():
#     request = request.get
#
#     if not position:
#         return jsonify({"error": "Position is required"}), 400
#     players = get_players_by_position(position)
#     return players


@teams_bp.route('/', methods=['POST'])
def create_team():
    data = request.get_json()
    result = insert_team(data)
    if result.get('error'):
        return jsonify(result), 400
    return jsonify(result), 201
