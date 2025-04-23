import json
from services.services import get
from constant import API_FOOTBALL, ENVIRONMENT


async def get_team_stadistics(league, season, team, date):
    if ENVIRONMENT == "dev":
        with open("./json/team_stadistics.json") as f:
            jts = json.load(f)
            return jts

    response = get(API_FOOTBALL["API_URI_TEAM_STADISTICS"], league, season, team, date)
    return response


"""
TBD	Time To Be Defined	Scheduled	Scheduled but date and time are not known
NS	Not Started	Scheduled	
1H	First Half, Kick Off	In Play	First half in play
HT	Halftime	In Play	Finished in the regular time
2H	Second Half, 2nd Half Started	In Play	Second half in play
ET	Extra Time	In Play	Extra time in play
BT	Break Time	In Play	Break during extra time
P	Penalty In Progress	In Play	Penaly played after extra time
SUSP	Match Suspended	In Play	Suspended by referee's decision, may be rescheduled another day
INT	Match Interrupted	In Play	Interrupted by referee's decision, should resume in a few minutes
FT	Match Finished	Finished	Finished in the regular time
AET	Match Finished	Finished	Finished after extra time without going to the penalty shootout
PEN	Match Finished	Finished	Finished after the penalty shootout
PST	Match Postponed	Postponed	Postponed to another day, once the new date and time is known the status will change to Not Started
CANC	Match Cancelled	Cancelled	Cancelled, match will not be played
ABD	Match Abandoned	Abandoned	Abandoned for various reasons (Bad Weather, Safety, Floodlights, Playing Staff Or Referees), Can be rescheduled or not, it depends on the competition
AWD	Technical Loss	Not Played	
WO	WalkOver	Not Played	Victory by forfeit or absence of competitor
LIVE	In Progress	In Play	Used in very rare cases. It indicates a fixture in progress but the data indicating the half-time or elapsed time are not available
"""


def get_fixtures(league, season, team, status, date):
    response = get(API_FOOTBALL["API_URI_FIXTURES"], league, season, team, status, date)
    return response


def get_injuries(league, season, team, date):
    response = get(API_FOOTBALL["API_URI_INJURIES"], league, season, team, date)
    return response


def get_standings(fixture):
    response = get(API_FOOTBALL["API_URI_FIXTURES_STANDING"], fixture)
    return response


def get_lineups(fixture):
    response = get(API_FOOTBALL["API_URI_FIXTURES_LINEUPS"], fixture)
    return response


async def get_statistics(fixture, team):
    response = get(API_FOOTBALL["API_URI_FIXTURES_STATISTICS"], fixture, team)
    return response


def get_player_statistics(fixture, team):
    response = get(API_FOOTBALL["API_URI_FIXTURES_PLAYER_STATISTICS"], fixture, team)
    return response


def get_h2h(ids_separate_with_line: str):
    response = get(API_FOOTBALL["API_URI_FIXTURES_H2H"], ids_separate_with_line)
    return response


def get_prediction(fixture):
    response = get(API_FOOTBALL["API_URI_PREDICTIONS"], fixture)
    return response
