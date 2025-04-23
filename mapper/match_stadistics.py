import json
from constant import API_FOOTBALL
from models.match_overview import MatchOverview
from models.team_overview import TeamOverview
from models.enum.statistics_types import StatisticsTypes
from models.enum.label_averages import LabelAverages
from services.football import get_team_stadistics, get_statistics, get_fixtures


def sync_match_stadistics(league, season, team, date):

    json_fixtures = get_fixtures(
        league, season, team, API_FOOTBALL["MATCHES_STATUS"], date
    )["response"][0]

    fixtures_with_statistics = map_fixtures_and_statistics_by_team(json_fixtures, team)

    averages = calculate_statistics_averages(fixtures_with_statistics, team)


def map_fixtures_and_statistics_by_team(json_fixtures, team):
    fixtures = []
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
            StatisticsTypes.PASSES_ACCURATE: passes_accurate,
        }
    return fixtures


def map_team_stadistics(league, season, team, date):
    team_overview = TeamOverview()
    json_team_stadistics = get_team_stadistics(league, season, team, date)
    return None


def calculate_statistics_averages(fixtures_with_statistics, team):
    averages = {}
    average_whole_shoots = 0
    average_shots_on_goal = 0
    average_shots_off_goal = 0
    average_shots_insidebox = 0
    average_shots_outsidebox = 0
    average_blocked_shots = 0
    average_fouls = 0
    average_offsides = 0
    average_corners = 0
    average_ball_possession = 0
    average_goalkeeper_saves = 0
    average_yellow_cards = 0
    average_red_cards = 0
    average_passes = 0
    average_passes_average = 0

    for fixture in fixtures_with_statistics:
        average_whole_shoots += fixture[StatisticsTypes.SHOTS_ON_GOAL]
        average_shots_on_goal += fixture[StatisticsTypes.SHOTS_ON_GOAL]
        average_shots_off_goal += fixture[StatisticsTypes.SHOTS_OFF_GOAL]
        average_shots_insidebox += fixture[StatisticsTypes.SHOTS_INSIDEBOX]
        average_shots_outsidebox += fixture[StatisticsTypes.SHOTS_OUTSIDEBOX]
        average_blocked_shots += fixture[StatisticsTypes.BLOCKED_SHOTS]
        average_fouls += fixture[StatisticsTypes.FOULS]
        average_corners += fixture[StatisticsTypes.CORNER_KICKS]
        average_offsides += fixture[StatisticsTypes.OFFSIDES]
        average_ball_possession += fixture[StatisticsTypes.BALL_POSSESSION]
        average_goalkeeper_saves += fixture[StatisticsTypes.GOALKEEPER_SAVES]
        average_yellow_cards += fixture[StatisticsTypes.YELLOW_CARD]
        average_red_cards += fixture[StatisticsTypes.RED_CARD]
        average_passes += fixture[StatisticsTypes.TOTAL_PASSES]
        average_passes_average += fixture[StatisticsTypes.PASSES_ACCURATE]
    
    average_whole_shoots = average_whole_shoots / len(fixtures_with_statistics)
    average_shots_on_goal = average_shots_on_goal / len(fixtures_with_statistics)
    average_shots_off_goal = average_shots_off_goal / len(fixtures_with_statistics)
    average_shots_insidebox = average_shots_insidebox / len(fixtures_with_statistics)
    average_shots_outsidebox = average_shots_outsidebox / len(fixtures_with_statistics)
    average_blocked_shots = average_blocked_shots / len(fixtures_with_statistics)
    average_fouls = average_fouls / len(fixtures_with_statistics)
    average_offsides = average_offsides / len(fixtures_with_statistics)
    average_ball_possession = average_ball_possession / len(fixtures_with_statistics)
    average_goalkeeper_saves = average_goalkeeper_saves / len(fixtures_with_statistics)
    average_yellow_cards = average_yellow_cards / len(fixtures_with_statistics)
    average_red_cards = average_red_cards / len(fixtures_with_statistics)
    average_passes = average_passes / len(fixtures_with_statistics)
    average_passes_average = average_passes_average / len(fixtures_with_statistics)

    passes = {
        LabelAverages.TOTAL: average_passes,
        LabelAverages.PASSES_ACCURATE: average_passes_average
    }

    total_shoots_average = (average_shots_insidebox + average_shots_outsidebox + average_shots_on_goal + average_shots_off_goal) / 4

    shots = {
        LabelAverages.TOTAL: total_shoots_average,
        LabelAverages.ON_GOAL: average_shots_on_goal,
        LabelAverages.OFF_GOAL: average_shots_off_goal,
        LabelAverages.BLOCKED: average_blocked_shots,
        LabelAverages.INSIDEBOX: average_shots_insidebox,
        LabelAverages.OUTSIDEBOX: average_shots_outsidebox
    }

    cards = {
        LabelAverages.YELLOW : average_yellow_cards,
        LabelAverages.RED : average_red_cards
    }

    averages = {
        team:{
            LabelAverages.GOALS: 0,
            LabelAverages.CORNERS: average_corners,
            LabelAverages.FOULS: average_fouls,
            LabelAverages.OFFSIDES: average_offsides,
            LabelAverages.POSSESION: average_ball_possession,
            LabelAverages.GOALKEEPER_SAVES: average_goalkeeper_saves,
            LabelAverages.PASSES: passes,
            LabelAverages.SHOTS: shots,
            LabelAverages.CARDS: cards
        }
    }

    return averages


def set_averages():
    average = {
        "goals": 0,
        "corners": 2,
        "fouls": 0,
        "offsides": 0,
        "possesion": 0,
        "goalkeeper_saves": 0,
        "passes": {"total": 0, "accurate": "10%"},
        "shots": {
            "total": 3,
            "on_goal": 4,
            "off_goal": 0,
            "blocked": 0,
            "insidebox": 0,
            "outsidebox": 0,
        },
        "cards": {
            "red": 3,
            "yellow": 2,
        },
    }
