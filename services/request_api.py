import requests
from db import db
import json
from models.players import PlayerStats

year_2022 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/2022'
year_2023 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/2023'
year_2024 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/2024'
all_years = [year_2022, year_2023, year_2024]


def get_players_by_season(year):
    # for year in all_years:
    url_players = f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/{year}'
    response = requests.get(url_players)
    if response.status_code == 200:
        data = response.json()
        # print(data)
    else:
        return
    # data = response.json()
    # lst_data = json.load(data)
    # for player in data:
    #     player_id = player['PlayerID']
    #     player_name = player['PlayerName']
    #     position = player['Position']
    #     games = player['Games']
    #     field_goals = player['FieldGoals']
    #     three_percent = player['ThreePercent']
    #     two_percent = player['TwoPercent']
    #     assists = player['Assists']
    #     turnovers = player['Turnovers']
    #     points = player['Points']
    #     team = player['Team']
    #     season = player['Season']

    dct_average_ppg_by_position = calc_all_position_ppg(data)
    for player in data:
        print(player)
        atr = calculate_ATR(player)
        ppg_ratio = calculate_ppg_player(dct_average_ppg_by_position, player)
        player_stats = PlayerStats(player_id=player.get('playerId'), player_name=player.get('playerName'),
                                   position=player.get('position'), games=player.get('games', 0.0),
                                   field_goals=player.get('fieldGoals', 0.0), three_percent=player.get('threePercent',0.0),
                                   two_percent=player.get('twoPercent', 0.0), assists=player.get('assists', 0.0),
                                   turnovers=player.get('turnovers', 0.0), points=player.get('points', 0.0),
                                   team=player.get('team', ""), season=player.get('season', 0), ATR=atr, PPG_ratio=ppg_ratio)
        db.session.add(player_stats)
    db.session.commit()
    return

def calculate_ATR(dict_player):
    if dict_player['points'] == 0:
        return 0
    return dict_player['assists'] / dict_player['points']





def calc_ppg_to_position(lst_players, position):
    points = 0
    games = 0
    for player in lst_players:
        if player['position'] == position:
            points += player['points']
            games += player['games']

    if games == 0:
        return 0
    return points / games

def calc_all_position_ppg(lst_players):
    ppg_ratio = {}
    for position in ['PG', 'SG', 'SF', 'PF', 'C']:
        ppg_ratio[position] = calc_ppg_to_position(lst_players, position)
    return ppg_ratio

# calculate ppg for player by divide average of the player by average of his position
def calculate_ppg_player(dct_positions, dct_player):
    if dct_player['games'] == 0:
        return 0
    player_position = dct_player.get('position')
    if player_position and len(player_position) > 2:
        if player_position[1] == '-':
            player_position = player_position[0]
        else:
            player_position = player_position[0:2]
    print(player_position)
    return dct_player['points'] / dct_player['games'] / dct_positions[player_position]


