import json

from flask import Blueprint

from ..services.apitennis.apitennis import get_H2H

h2h_api = Blueprint("h2h_api", __name__)


@h2h_api.route("/h2h/<first_player_key>/<second_player_key>")
def h2h(first_player_key: str, second_player_key: str):
    """H2H service specification.
            ---
    parameters:
          - name: first_player_key
            in: path
            type: string
            required: true
            description: First player to compare
          - name: second_player_key
            in: path
            type: string
            required: true
            description: Final player to compare
            responses:
              200:
                description: A list of events
                schema:
                  $ref: '#/definitions/H2H'
                examples: {
                "success": 1,
                "result": {
                        "H2H": [],
                        "firstPlayerResults": [
                                {
                                        "event_key": "112163",
                                        "event_date": "2022-05-11",
                                        "event_time": "15:00",
                                        "event_first_player": "Cervantes Tomas/ Ferrer Adria",
                                        "first_player_key": "2616",
                                        "event_second_player": "Kravchenko/ Reymond",
                                        "second_player_key": "2316",
                                        "event_final_result": "0 - 2",
                                        "event_game_result": "-",
                                        "event_serve": null,
                                        "event_winner": "Second Player",
                                        "event_status": "Finished",
                                        "event_type_type": "Itf Men Doubles",
                                        "tournament_name": "ITF M15 Ulcinj Men",
                                        "tournament_key": "4561",
                                        "tournament_round": "ITF M15 Ulcinj Men - 1/8-finals",
                                        "tournament_season": "2022",
                                        "event_live": "0",
                                        "event_first_player_logo": null,
                                        "event_second_player_logo": null
                                }],
                                "secondPlayerResults": [
                                {
                                        "event_key": "94804",
                                        "event_date": "2022-05-11",
                                        "event_time": "15:10",
                                        "event_first_player": "Lopez San Martin/ Rincon",
                                        "first_player_key": "2139",
                                        "event_second_player": "Regas/ Vasershtein",
                                        "second_player_key": "2617",
                                        "event_final_result": "2 - 0",
                                        "event_game_result": "-",
                                        "event_serve": null,
                                        "event_winner": "First Player",
                                        "event_status": "Finished",
                                        "event_type_type": "Itf Men Doubles",
                                        "tournament_name": "ITF M15 Valldoreix Men",
                                        "tournament_key": "3855",
                                        "tournament_round": "ITF M15 Valldoreix Men - Quarter-finals",
                                        "tournament_season": "2022",
                                        "event_live": "0",
                                        "event_first_player_logo": null,
                                        "event_second_player_logo": null
                                }
                ]
          }
        }
    """
    return get_H2H(
        first_player_key=first_player_key, second_player_key=second_player_key
    )
