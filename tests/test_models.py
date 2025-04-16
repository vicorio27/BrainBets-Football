import json
import logging

from models.event import Event
from wrapper.response import Response


def test_event_wrapper():
    with open("./json/events.json") as f:
        jevents = json.load(f)
        events = Response(**jevents)
        assert jevents["success"] == events.success


def test_fixtures_wrapper():
    with open("./json/fixtures.json") as f:
        jfixtures = json.load(f)
        fixtures = Response(**jfixtures)
        assert jfixtures["success"] == fixtures.success


def test_h2h_wrapper():
    with open("./json/H2H.json") as f:
        jh2h = json.load(f)
        h2h = Response(**jh2h)
        assert jh2h["success"] == h2h.success


def test_livescore_wrapper():
    with open("./json/livescore.json") as f:
        jlivescore = json.load(f)
        livescore = Response(**jlivescore)
        assert jlivescore["success"] == livescore.success


def test_standing_wrapper():
    with open("./json/standings.json") as f:
        jstanding = json.load(f)
        standing = Response(**jstanding)
        assert jstanding["success"] == standing.success


def test_player_wrapper():
    with open("./json/players.json") as f:
        jplayer = json.load(f)
        player = Response(**jplayer)
        assert jplayer["success"] == player.success


def test_tournament_wrapper():
    with open("./json/tournaments.json") as f:
        jtournament = json.load(f)
        tournament = Response(**jtournament)
        assert jtournament["success"] == tournament.success
