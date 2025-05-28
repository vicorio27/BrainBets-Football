from constant import API_FOOTBALL
from models.enum.team_stadistics import TeamStadisticsTypes
from models.team_overview import TeamOverview
from models.enum.statistics_types import StatisticsTypes
from models.enum.label_averages import LabelAverages
from services.football import get_team_stadistics, get_statistics, get_fixtures
from utils.calculationsutils import calculate_best_lineup, calculate_best_minutes, calculate_best_time_to_get_cards, calculate_best_under_over


def get_and_map_team_stadistics(league, season, team, date):

    json_fixtures = get_fixtures(
        league, season, team, API_FOOTBALL["API_URI_FIXTURES"], date
    )["response"]

    fixtures_with_statistics = map_fixtures_and_statistics_by_team(json_fixtures, team)

    averages = calculate_statistics_averages_by_team(fixtures_with_statistics)

    team_overview = map_team_averages_and_stadistics(averages, league, season, team, date)

    return team_overview


def map_fixtures_and_statistics_by_team(json_fixtures, team):
    fixtures = []
    for fixture in json_fixtures:
        local_goal = 0
        away_goal = 0
        local_halftime_goal = 0
        away_halftime_goal = 0
        local_fulltime_goal = 0
        away_fulltime_goal = 0
        local_extratime_goal = 0
        away_extratime_goal = 0
        local_penalty = 0
        away_penalty = 0
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
        json_statistics = get_statistics(fixture["fixture"]["id"], team)["response"][0][
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
                case StatisticsTypes.PASSES_ACCURATE:
                    passes_accurate += statistics["value"]
                case _:
                    print("Metrica no encontrada: " + statistics["type"])

        local_goal += fixture["goals"]["home"]
        away_goal += fixture["goals"]["away"]
        local_halftime_goal += fixture["score"]["halftime"]["home"]
        away_halftime_goal += fixture["score"]["halftime"]["away"]

        local_fulltime_goal += (
            fixture["score"]["fulltime"]["home"]
            if fixture["score"]["fulltime"]["home"]
            else 0
        )
        away_fulltime_goal += (
            fixture["score"]["fulltime"]["away"]
            if fixture["score"]["fulltime"]["away"]
            else 0
        )

        local_extratime_goal += (
            fixture["score"]["extratime"]["home"]
            if fixture["score"]["extratime"]["home"]
            else 0
        )
        away_extratime_goal += (
            fixture["score"]["extratime"]["away"]
            if fixture["score"]["extratime"]["away"]
            else 0
        )

        local_penalty += (
            fixture["score"]["penalty"]["home"]
            if fixture["score"]["penalty"]["home"]
            else 0
        )
        away_penalty += (
            fixture["score"]["penalty"]["away"]
            if fixture["score"]["penalty"]["away"]
            else 0
        )

        fixtures[fixture["fixture"]["id"]] = {
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
            StatisticsTypes.LOCAL_GOALS: local_goal,
            StatisticsTypes.AWAY_GOALS: away_goal,
            StatisticsTypes.LOCAL_HALFTIME_GOALS: local_halftime_goal,
            StatisticsTypes.AWAY_HALFTIME_GOALS: away_halftime_goal,
            StatisticsTypes.LOCAL_FULLTIME_GOALS: local_fulltime_goal,
            StatisticsTypes.AWAY_FULLTIME_GOALS: away_fulltime_goal,
            StatisticsTypes.LOCAL_EXTRATIME_GOALS: local_extratime_goal,
            StatisticsTypes.AWAY_EXTRATIME_GOALS: away_extratime_goal,
            StatisticsTypes.LOCAL_PENALTY: local_penalty,
            StatisticsTypes.AWAY_PENTALTY: away_penalty,
        }

    return fixtures


def calculate_statistics_averages_by_team(fixtures_with_statistics):
    averages = {}
    average_local_goal = 0
    average_away_goal = 0
    average_local_halftime_goal = 0
    average_away_halftime_goal = 0
    average_local_fulltime_goal = 0
    average_away_fulltime_goal = 0
    average_local_extratime_goal = 0
    average_away_extratime_goal = 0
    average_local_penalty = 0
    average_away_penalty = 0
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
        average_local_goal += fixture[StatisticsTypes.LOCAL_GOALS]
        average_away_goal += fixture[StatisticsTypes.AWAY_GOALS]
        average_local_halftime_goal += fixture[StatisticsTypes.LOCAL_HALFTIME_GOALS]
        average_away_halftime_goal += fixture[StatisticsTypes.AWAY_HALFTIME_GOALS]
        average_local_fulltime_goal += fixture[StatisticsTypes.LOCAL_FULLTIME_GOALS]
        average_away_fulltime_goal += fixture[StatisticsTypes.AWAY_FULLTIME_GOALS]
        average_local_extratime_goal += fixture[StatisticsTypes.LOCAL_EXTRATIME_GOALS]
        average_away_extratime_goal += fixture[StatisticsTypes.AWAY_EXTRATIME_GOALS]
        average_local_penalty += fixture[StatisticsTypes.LOCAL_PENALTY]
        average_away_penalty += fixture[StatisticsTypes.AWAY_PENTALTY]

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
    # goals
    average_local_goal = average_local_goal / len(fixtures_with_statistics)
    average_away_goal = average_away_goal / len(fixtures_with_statistics)
    average_local_halftime_goal = average_local_halftime_goal / len(
        fixtures_with_statistics
    )
    average_away_halftime_goal = average_away_halftime_goal / len(
        fixtures_with_statistics
    )
    average_local_fulltime_goal = average_local_fulltime_goal / len(
        fixtures_with_statistics
    )
    average_away_fulltime_goal = average_away_fulltime_goal / len(
        fixtures_with_statistics
    )
    average_local_extratime_goal = average_local_extratime_goal / len(
        fixtures_with_statistics
    )
    average_away_extratime_goal = average_away_extratime_goal / len(
        fixtures_with_statistics
    )
    average_local_penalty = average_local_penalty / len(fixtures_with_statistics)
    average_away_penalty = average_away_penalty / len(fixtures_with_statistics)

    goals = {
        LabelAverages.LOCAL_GOALS: average_local_goal,
        LabelAverages.AWAY_GOALS: average_away_goal,
        LabelAverages.LOCAL_HALFTIME_GOALS: average_local_halftime_goal,
        LabelAverages.AWAY_HALFTIME_GOALS: average_away_halftime_goal,
        LabelAverages.LOCAL_FULLTIME_GOALS: average_local_fulltime_goal,
        LabelAverages.AWAY_FULLTIME_GOALS: average_away_fulltime_goal,
        LabelAverages.LOCAL_EXTRATIME_GOALS: average_local_extratime_goal,
        LabelAverages.AWAY_EXTRATIME_GOALS: average_away_extratime_goal,
        LabelAverages.LOCAL_PENALTY: average_local_penalty,
        LabelAverages.AWAY_PENALTY: average_away_penalty,
    }

    passes = {
        LabelAverages.TOTAL: average_passes,
        LabelAverages.PASSES_ACCURATE: average_passes_average,
    }

    total_shoots_average = (
        average_shots_insidebox
        + average_shots_outsidebox
        + average_shots_on_goal
        + average_shots_off_goal
    ) / 4

    shots = {
        LabelAverages.TOTAL: total_shoots_average,
        LabelAverages.ON_GOAL: average_shots_on_goal,
        LabelAverages.OFF_GOAL: average_shots_off_goal,
        LabelAverages.BLOCKED: average_blocked_shots,
        LabelAverages.INSIDEBOX: average_shots_insidebox,
        LabelAverages.OUTSIDEBOX: average_shots_outsidebox,
    }

    cards = {
        LabelAverages.YELLOW: average_yellow_cards,
        LabelAverages.RED: average_red_cards,
    }

    averages = {
            LabelAverages.GOALS: goals,
            LabelAverages.CORNERS: average_corners,
            LabelAverages.FOULS: average_fouls,
            LabelAverages.OFFSIDES: average_offsides,
            LabelAverages.POSSESION: average_ball_possession,
            LabelAverages.GOALKEEPER_SAVES: average_goalkeeper_saves,
            LabelAverages.PASSES: passes,
            LabelAverages.SHOTS: shots,
            LabelAverages.CARDS: cards,
    }

    return averages


def map_team_averages_and_stadistics(averages, league, season, team, date):
    team_overview = TeamOverview()
    json_team_stadistics = get_team_stadistics(league, season, team, date)["response"]

    fixtures = json_team_stadistics["fixtures"]
    goals = json_team_stadistics["goals"]
    biggest = json_team_stadistics["biggest"]
    cards = json_team_stadistics["cards"]

    goals_for = goals["for"]
    goals_for_minute = goals_for["minute"]
    goals_against = goals["against"]
    goals_against_minute = goals_against["minute"]

    under_over = goals["under_over"]

    local_played_games = fixtures["played"]["home"]
    away_played_games = fixtures["played"]["away"]
    total_played_games = fixtures["played"]["total"]

    local_wins_games = fixtures["wins"]["home"]
    away_wins_games = fixtures["wins"]["away"]
    total_wins_games = fixtures["wins"]["total"]

    local_draws_games = fixtures["draws"]["home"]
    away_draws_games = fixtures["draws"]["away"]
    total_draws_games = fixtures["draws"]["total"]

    local_loses_games = fixtures["loses"]["home"]
    away_loses_games = fixtures["loses"]["away"]
    total_loses_games = fixtures["loses"]["total"]

    scored_home_goals = goals_for["total"]["home"]
    scored_away_goals = goals_for["total"]["away"]
    scored_total_goals = goals_for["total"]["total"]

    scored_home_goals_average = goals_for["average"]["home"]
    scored_away_goals_average = goals_for["average"]["away"]
    scored_total_goals_average = goals_for["average"]["total"]

    best_time_scored_goals = calculate_best_minutes(goals_for_minute)
    best_time_against_goals = calculate_best_minutes(goals_against_minute)
    best_under, best_over = calculate_best_under_over(under_over)

    best_lineup = calculate_best_lineup(json_team_stadistics["lineups"])
    best_time_yellow_cards = calculate_best_time_to_get_cards(cards["yellow"])
    best_time_red_cards = calculate_best_time_to_get_cards(cards["red"])

    home_matches = {
        TeamStadisticsTypes.LOCAL_PLAYED_GAMES: local_played_games,
        TeamStadisticsTypes.LOCAL_WINS: local_wins_games,
        TeamStadisticsTypes.LOCAL_DRAWS: local_draws_games,
        TeamStadisticsTypes.LOCAL_LOSES: local_loses_games,
    }
    away_matches = {
        TeamStadisticsTypes.AWAY_PLAYED_GAMES: away_played_games,
        TeamStadisticsTypes.AWAY_WINS: away_wins_games,
        TeamStadisticsTypes.AWAY_DRAWS: away_draws_games,
        TeamStadisticsTypes.AWAY_LOSES: away_loses_games,
    }
    total_matches = {
        TeamStadisticsTypes.TOTAL_PLAYED_GAMES: total_played_games,
        TeamStadisticsTypes.TOTAL_WINS: total_wins_games,
        TeamStadisticsTypes.TOTAL_DRAWS: total_draws_games,
        TeamStadisticsTypes.TOTAL_LOSES: total_loses_games,
    }

    goals_scored = {
        TeamStadisticsTypes.LOCAL_SCORED_GOAL: scored_home_goals,
        TeamStadisticsTypes.LOCAL_AVERAGE_SCORED_GOAL: scored_home_goals_average,
        TeamStadisticsTypes.TOTAL_LOCAL_SCORED_GOAL: scored_total_goals,
        TeamStadisticsTypes.TOTAL_LOCAL_AVERAGE_SCORED_GOAL: scored_total_goals_average,
    }

    goals_against = {
        TeamStadisticsTypes.AWAY_SCORED_GOAL: scored_away_goals,
        TeamStadisticsTypes.AWAY_AVERAGE_SCORED_GOAL: scored_away_goals_average,
    }

    goals = {
        TeamStadisticsTypes.BEST_TIME_GOAL_SCORED: best_time_scored_goals,
        TeamStadisticsTypes.BEST_TIME_GOAL_AGAINST: best_time_against_goals,
    }

    to_score = {
        TeamStadisticsTypes.TO_SCORED: goals,
    }

    yellow_cards = {TeamStadisticsTypes.YELLOW_CARDS: best_time_yellow_cards}

    red_cards = {TeamStadisticsTypes.RED_CARDS: best_time_red_cards}

    to_get_cards = {
        TeamStadisticsTypes.YELLOW_CARDS: yellow_cards,
        TeamStadisticsTypes.RED_CARDS: red_cards,
    }

    biggest_home = {
        TeamStadisticsTypes.BIGGEST_HOME_WIN: biggest["wins"]["home"],
        TeamStadisticsTypes.BIGGEST_HOME_LOSS: biggest["loses"]["home"],
        TeamStadisticsTypes.BIGGEST_HOME_SCORED_GOALS: biggest["goals"]["for"]["home"],
        TeamStadisticsTypes.BIGGEST_HOME_GOALS_AGAINST: biggest["goals"]["against"][
            "home"
        ],
    }

    biggest_away = {
        TeamStadisticsTypes.BIGGEST_AWAY_WIN: biggest["wins"]["away"],
        TeamStadisticsTypes.BIGGEST_AWAY_LOSS: biggest["loses"]["away"],
        TeamStadisticsTypes.BIGGEST_AWAY_SCORED_GOALS: biggest["goals"]["for"]["away"],
        TeamStadisticsTypes.BIGGEST_AWAY_GOALS_AGAINST: biggest["goals"]["against"][
            "away"
        ],
    }

    clean_sheet = {
        TeamStadisticsTypes.TOTAL: json_team_stadistics["clean_sheet"]["total"],
    }

    matches = {
        TeamStadisticsTypes.TOTAL: total_matches,
    }

    failed_score = {
        TeamStadisticsTypes.TOTAL_FAILED_SCORE: json_team_stadistics["failed_to_score"][
            "total"
        ],
    }

    penalty_totals = {
        TeamStadisticsTypes.TOTAL_PENALTY: json_team_stadistics["penalty"]["total"],
        TeamStadisticsTypes.PENALTY_SCORED: json_team_stadistics["penalty"]["scored"][
            "total"
        ],
        TeamStadisticsTypes.PENALTY_MISSED: json_team_stadistics["penalty"]["missed"][
            "total"
        ],
    }

    best_lineup = {
        TeamStadisticsTypes.MOST_COMMON_LINEUP: best_lineup["formation"],
        TeamStadisticsTypes.LARGEST_NUMBER_COMMON_LINEUP: best_lineup["played"],
    }

    streak = {
        TeamStadisticsTypes.STREAKS_WINS: biggest["streak"]["wins"],
        TeamStadisticsTypes.STREAKS_DRAW: biggest["streak"]["draws"],
        TeamStadisticsTypes.STREAKS_LOSES: biggest["streak"]["loses"],
    }

    totals = {
        TeamStadisticsTypes.CLEAN_TOTAL_SHEET: clean_sheet,
        TeamStadisticsTypes.TOTAL: matches,
        TeamStadisticsTypes.TOTAL_FAILED_SCORE: failed_score,
        TeamStadisticsTypes.TOTAL_PENALTY: penalty_totals,
    }

    penalty_percentage = {
        TeamStadisticsTypes.PERCENTAGE_PENALTY_SCORED: json_team_stadistics["penalty"][
            "scored"
        ]["percentage"],
        TeamStadisticsTypes.PERCENTAGE_PENALTY_MISSED: json_team_stadistics["penalty"][
            "missed"
        ]["percentage"],
    }

    home = {
        TeamStadisticsTypes.MATCHES: home_matches,
        TeamStadisticsTypes.GOALS: goals_scored,
        TeamStadisticsTypes.BIGGEST: biggest_home,
        TeamStadisticsTypes.CLEAN_HOME_SHEET: json_team_stadistics["clean_sheet"][
            "home"
        ],
        TeamStadisticsTypes.FAILED_TO_SCORE_HOME: json_team_stadistics[
            "failed_to_score"
        ]["home"],
    }

    away = {
        TeamStadisticsTypes.MATCHES: away_matches,
        TeamStadisticsTypes.GOALS: goals_against,
        TeamStadisticsTypes.BIGGEST: biggest_away,
        TeamStadisticsTypes.CLEAN_AWAY_SHEET: json_team_stadistics["clean_sheet"][
            "away"
        ],
        TeamStadisticsTypes.FAILED_TO_SCORE_AWAY: json_team_stadistics[
            "failed_to_score"
        ]["away"],
    }

    best_times = {
        TeamStadisticsTypes.GOALS: to_score,
        TeamStadisticsTypes.CARDS: to_get_cards,
        TeamStadisticsTypes.UNDER: best_under,
        TeamStadisticsTypes.OVER: best_over,
        TeamStadisticsTypes.LINEUPS: best_lineup,
    }

    team_overview.name = team
    team_overview.home = home
    team_overview.away = away
    team_overview.averages = averages
    team_overview.totals = totals
    team_overview.streak = streak
    team_overview.best_time = best_times
    team_overview.percentages[penalty_percentage] = penalty_percentage

    return team_overview
