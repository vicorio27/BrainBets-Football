from flask import Blueprint

from ..services.apitennis.apitennis import get_ranking

ranking_api = Blueprint("ranking_api", __name__)


@ranking_api.route("/ranking/<event_type>")
def ranking(event_type: str):
    """Ranking/Standings service specification.
    ---
    parameters:
    - name: event_type
    in: path
    type: string
    enum: ['ATP', 'WTA']
    required: true
    description: First player to compare
    definitions:
      Ranking:
        type: object
    responses:
      200:
        description: A list of Rankings
        schema:
          $ref: '#/definitions/Ranking'
        examples: {
            "success": 1,
            "result": [
                {
                        "event_type_key": "267",
                        "event_type_type": "Atp Doubles"
                },
                {
                        "event_type_key": "265",
                        "event_type_type": "Atp Singles"
                }
            ]
        }
    """
    return get_ranking(event_type=event_type)
