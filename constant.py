import os

TIME_ZONE = "America/New_York"
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
CONTENT_TYPE = "application/json"

API_FOOTBALL = {
    "API": "https://v3.football.api-sports.io",
    "API_KEY": os.environ.get("API_TENNIS_KEY", "6822888ac2f21a885c856c17229faeef"),
    "API_HOST": "v3.football.api-sports.io",
    "API_URI_LEAGUES": "/leagues",
    "API_URI_TEAMS": "/teams",
    "API_URI_STANDING": "/standings",
    "API_URI_INJURIES": "/injuries",
    "API_URI_TEAM_STADISTICS": "/teams/statistics",
    "API_URI_FIXTURES": "/fixtures",
    "API_URI_FIXTURES_H2H": "/fixtures/headtohead",
    "API_URI_FIXTURES_STATISTICS": "/fixtures/statistics",
    "API_URI_FIXTURES_LINEUPS": "/fixtures/lineups",
    "API_URI_FIXTURES_PLAYER_STATISTICS": "/fixtures/players",
    "API_URI_PREDICTIONS": "/predictions",
    "MATCHES_STATUS": "FT-AET-PEN" "STATISTICS_TYPES",
}
