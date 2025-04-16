import os

TIME_ZONE = "America/New_York"
ENVIRONMENT = (os.environ.get("ENVIRONMENT", "dev"),)

API_TENNIS = {
    "API": "https://api.api-tennis.com/tennis/",
    "APIKEY": os.environ.get("API_TENNIS_KEY"),
    "METHOD_GET_EVENTS": "get_events",
    "METHOD_GET_TOURNAMENTS": "get_tournaments",
    "METHOD_GET_FIXTURES": "get_fixtures",
    "METHOD_GET_LIVESCORE": "get_livescore",
    "METHOD_H2H": "get_H2H",
    "METHOD_STANDINGS": "get_standings",
    "METHOD_PLAYERS": "get_players",
}
