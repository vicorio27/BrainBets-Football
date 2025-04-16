import json

from flask import Blueprint
from ..services.apitennis.apitennis import get_fixtures

events_api = Blueprint("events_api", __name__)


@events_api.route("/fixtures")
def fixtures(
    date_start: str,
    date_stop: str,
    event_type_key: str,
    tournament_key: str,
    match_key: str,
    player_key: str,
):
    """Fixtures service specification.
                ---
        parameters:
              - name: date_start
                in: path
                type: string
                required: true
                description: Start date to filter
              - name: date_stop
                in: path
                type: string
                required: true
                description: Stop final date to filter
              - name: event_type_key
                in: path
                type: string
                required: true
                description: event type key
              - name: tournament_key
                in: path
                type: string
                required: true
                description: tournament type key
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
                    description: A list of fixtures
                    schema:
                      $ref: '#/definitions/H2H'
                    examples: {
        "success": 1,
        "result": [
            {
                "event_key": "143104",
                "event_date": "2022-06-17",
                "event_time": "18:00",
                "event_first_player": "M. Navone",
                "first_player_key": "949",
                "event_second_player": "C. Gomez-Herrera",
                "second_player_key": "3474",
                "event_final_result": "-",
                "event_game_result": "-",
                "event_serve": null,
                "event_winner": null,
                "event_status": "",
                "event_type_type": "Challenger Men Singles",
                "tournament_name": "Corrientes Challenger Men",
                "tournament_key": "2646",
                "tournament_round": "",
                "tournament_season": "2022",
                "event_live": "0",
                "event_qualification": "False",
                "event_first_player_logo": null,
                "event_second_player_logo": "https://api.api-tennis.com/logo-tennis/3474_c-gomez-herrera.jpg",
                "pointbypoint": [],
                "scores": []
            },
            {
                "event_key": "143113",
                "event_date": "2022-06-17",
                "event_time": "01:05",
                "event_first_player": "C. Chidekh",
                "first_player_key": "7102",
                "event_second_player": "M. Cassone",
                "second_player_key": "12744",
                "event_final_result": "2 - 0",
                "event_game_result": "-",
                "event_serve": null,
                "event_winner": "First Player",
                "event_status": "Finished",
                "event_type_type": "Itf Men Singles",
                "tournament_name": "ITF M25 Wichita, KS Men",
                "tournament_key": "4195",
                "tournament_round": "",
                "tournament_season": "2022",
                "event_live": "0",
                "event_first_player_logo": null,
                "event_second_player_logo": null,
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
                        "score_first": "6",
                        "score_second": "4",
                        "score_set": "1"
                    },
                    {
                        "score_first": "6",
                        "score_second": "2",
                        "score_set": "2"
                    }
                  ]
              }
      ]
    }
    """
    return get_fixtures(
        date_start=date_start,
        date_stop=date_stop,
        event_type_key=event_type_key,
        match_key=match_key,
        player_key=player_key,
        tournament_key=tournament_key,
    )
