import json
from services.services import get
from constant import API_FOOTBALL, ENVIRONMENT

def get_team_stadistics(league, season, team, date):
    if ENVIRONMENT == "dev":
        with open("./json/team_stadistics.json") as f:
            jts = json.load(f)
            return jts
        
    response = get(API_FOOTBALL["API_URI_TEAM_STADISTICS"], league, season, team, date)
    return response

