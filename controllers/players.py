import json

from flask import Blueprint
from ..services.apitennis.apitennis import get_players

players_api = Blueprint("players_api", __name__)


@players_api.route("/players/<player_key>/<tournament_key>")
def players(player_key: str, tournament_key: str):
    """Players service specification.
       ---
    parameters:
          - name: player_key
            in: path
            type: string
            required: true
            description: player key to evaluate
          - name: tournament_key
            in: path
            type: string
            required: true
            description: tournament key to evaluate plater performance
            definitions:
                Player:
                type: object
            responses:
                200:
                description: A list of players
                schema:
                    $ref: '#/definitions/Player'
                examples: {
                "success": 1,
                "result": [
                        {
                           "player_key": "1905",
                           "player_name": "N. Djokovic",
                           "player_country": "Serbia",
                           "player_bday": "22.05.1987",
                           "player_logo": "https://api.api-tennis.com/logo-tennis/1905_n-djokovic.jpg",
                           "stats": [
                                   {
                                           "season": "2021",
                                           "type": "doubles",
                                           "rank": "255",
                                           "titles": "0",
                                           "matches_won": "6",
                                           "matches_lost": "4",
                                           "hard_won": "2",
                                           "hard_lost": "2",
                                           "clay_won": "",
                                           "clay_lost": "",
                                           "grass_won": "3",
                                           "grass_lost": "0"
                                   },
                                   {
                                           "season": "2020",
                                           "type": "doubles",
                                           "rank": "158",
                                           "titles": "0",
                                           "matches_won": "2",
                                           "matches_lost": "1",
                                           "hard_won": "2",
                                           "hard_lost": "1",
                                           "clay_won": "",
                                           "clay_lost": "",
                                           "grass_won": "",
                                           "grass_lost": ""
                                   }
               ]
           }
        ]
    }
    """
    return get_players(player_key=player_key, tournament_key=tournament_key)
