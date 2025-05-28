from flask import Blueprint, request

from mapper.match_stadistics import get_and_map_team_stadistics
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
    return get_and_map_team_stadistics(league, season, team, date)


@team_stadistics_api.route("/match_stadistics")
def match_stadistics():
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
