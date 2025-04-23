import json

from flask import Blueprint, request
from ..services.football import get_team_stadistics

team_stadistics_api = Blueprint("team_stadistics_api", __name__)


@team_stadistics_api.route("/team_stadistics")
def team_stadistics():
    """Team stadistics service specification.
    ---
    definitions:
      TS:
        type: object
      Color:
        type: string
    responses:
      200:
        description: Team stadistics
        schema:
          $ref: '#/definitions/TeamStadistic'
    """
    league = request.args.get("league")
    team = request.args.get("team")
    # YYYY
    season = request.args.get("season")
    # YYYY-MM-DD
    date = request.args.get("date")
    return get_team_stadistics(league, season, team, date)
