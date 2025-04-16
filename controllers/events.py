import json

from flask import Blueprint
from ..services.apitennis.apitennis import get_events

events_api = Blueprint("events_api", __name__)


@events_api.route("/events")
def events():
    """Events service specification.
    ---
    definitions:
      Event:
        type: object
      Color:
        type: string
    responses:
      200:
        description: A list of events
        schema:
          $ref: '#/definitions/Event'
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
    return get_events()
