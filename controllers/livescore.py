import json

from flask import Blueprint
from ..services.apitennis.apitennis import get_live_scores

events_api = Blueprint("events_api", __name__)


@events_api.route("/livescore")
def livescore(
    event_type_key: str, tournament_key: str, match_key: str, player_key: str
):
    """Livescore service specification.
                ---
        parameters:
              - name: event_type_key
                in: path
                type: string
                required: true
                description: event type key
              - name: tournament_key
                in: path
                type: string
                required: true
                description: tournament key
              - name: match_key
                in: path
                type: string
                required: true
                description: match key
              - name: player_key
                in: path
                type: string
                required: true
                description: player key
                responses:
                  200:
                    description: A list of liverscore
                    schema:
                      $ref: '#/definitions/H2H'
                    examples: {
        "success": 1,
        "result": [
            {
                "event_key": "143192",
                "event_date": "2022-06-17",
                "event_time": "10:10",
                "event_first_player": "S. Bejlek",
                "first_player_key": "9393",
                "event_second_player": "R. Zarazua",
                "second_player_key": "1805",
                "event_final_result": "0 - 0",
                "event_game_result": "0 - 0",
                "event_serve": "First Player",
                "event_winner": null,
                "event_status": "Set 1",
                "event_type_type": "Itf Women Singles",
                "tournament_name": "ITF W60 Ceska Lipa Women",
                "tournament_key": "4210",
                "tournament_round": "",
                "tournament_season": "2022",
                "event_live": "1",
                "event_first_player_logo": null,
                "event_second_player_logo": "https://api.tennis.com/logo-tennis/1805_r-zarazua.jpg",
                "event_qualification": "False",
                "pointbypoint": [
                    {
                        "set_number": "Set 1",
                        "number_game": "1",
                        "player_served": "First Player",
                        "serve_winner": "First Player",
                        "serve_lost": null,
                        "score": "1 - 0",
                        "points": [
                            {
                                "number_point": "1",
                                "score": "15 - 0",
                                "break_point": null,
                                "set_point": null,
                                "match_point": null
                            }
                        ]
                    }
                ],
                "scores": [
                    {
                        "score_first": "5",
                        "score_second": "5",
                        "score_set": "1"
                    }
                ]
            }
        ]
    }
    """
    return get_live_scores(
        event_type_key=event_type_key,
        match_key=match_key,
        player_key=player_key,
        tournament_key=tournament_key,
    )
