import json
from constant import API_FOOTBALL
from models.match_overview import MatchOverview
from models.team_overview import TeamOverview
from models.statistics_types import StatisticsTypes
from services.football import get_team_stadistics, get_statistics, get_fixtures


async def sync_match_stadistics(league, season, team, date):
    team_overview = TeamOverview()
    json_team_stadistics = await get_team_stadistics(league, season, team, date)

    json_fixtures = get_fixtures(
        league, season, team, API_FOOTBALL["MATCHES_STATUS"], date
    )["response"][0]


def map_fixtures_and_statistics(json_fixtures, team):
    fixtures = {}
    for fixture in json_fixtures:
        shots_on_goal = 0
        shots_off_goal = 0
        total_shots = 0
        blocked_shots = 0
        shots_insidebox = 0
        shots_outsidebox = 0
        corners = 0
        fouls = 0
        offsides = 0
        ball_possession = 0
        yellow_cards = 0
        red_cards = 0
        goalkeeper_saves = 0
        total_passes = 0
        passes_accurate = 0
        json_statistics = get_statistics(fixture["id"], team)["response"][0][
            "statistics"
        ]
        for statistics in json_statistics:
            match statistics["type"]:
                case StatisticsTypes.SHOTS_ON_GOAL:
                    shots_on_goal += statistics["value"]
                case StatisticsTypes.SHOTS_OFF_GOAL:
                    shots_off_goal += statistics["value"]
                case StatisticsTypes.TOTAL_SHOTS:
                    total_shots += statistics["value"]
                case StatisticsTypes.BLOCKED_SHOTS:
                    blocked_shots += statistics["value"]
                case StatisticsTypes.SHOTS_INSIDEBOX:
                    shots_insidebox += statistics["value"]
                case StatisticsTypes.SHOTS_OUTSIDEBOX:
                    shots_outsidebox += statistics["value"]
                case StatisticsTypes.FOULS:
                    fouls += statistics["value"]
                case StatisticsTypes.CORNER_KICKS:
                    corners += statistics["value"]
                case StatisticsTypes.OFFSIDES:
                    offsides += statistics["value"]
                case StatisticsTypes.BALL_POSSESSION:
                    ball_possession += statistics["value"]
                case StatisticsTypes.YELLOW_CARD:
                    yellow_cards += statistics["value"]
                case StatisticsTypes.RED_CARD:
                    red_cards += statistics["value"]
                case StatisticsTypes.GOALKEEPER_SAVES:
                    goalkeeper_saves += statistics["value"]
                case StatisticsTypes.TOTAL_PASSES:
                    total_passes += statistics["value"]
                case StatisticsTypes.PASSES_ACURATE:
                    passes_accurate += statistics["value"]
                case _:
                    print("Metrica no encontrada: " + statistics["type"])
        fixtures[fixture["id"]] = {
            StatisticsTypes.SHOTS_ON_GOAL: shots_on_goal,
            StatisticsTypes.SHOTS_OFF_GOAL: shots_off_goal,
            StatisticsTypes.TOTAL_SHOTS: total_shots,
            StatisticsTypes.BLOCKED_SHOTS: blocked_shots,
            StatisticsTypes.SHOTS_INSIDEBOX: shots_insidebox,
            StatisticsTypes.SHOTS_OUTSIDEBOX: shots_outsidebox,
            StatisticsTypes.FOULS: fouls,
            StatisticsTypes.CORNER_KICKS: corners,
            StatisticsTypes.OFFSIDES: offsides,
            StatisticsTypes.BALL_POSSESSION: ball_possession,
            StatisticsTypes.YELLOW_CARD: yellow_cards,
            StatisticsTypes.RED_CARD: red_cards,
            StatisticsTypes.GOALKEEPER_SAVES: goalkeeper_saves,
            StatisticsTypes.TOTAL_PASSES: total_passes,
            StatisticsTypes.PASSES_ACURATE: passes_accurate,
        }
    return fixtures


def calculate_averages(json_team_stadistics):
    average = {
        "goal": json_team_stadistics["total"],
        "corners": 2,
        "shots": {"value": 3, "on_target": 4},
        "cards": {
            "red": 3,
            "yellow": 2,
        },
    }
