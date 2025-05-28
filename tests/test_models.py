import json

from wrapper.response import Response


def test_team_stadistics_wrapper():
    with open("./json/team_stadistics.json") as f:
        jts = json.load(f)
        team_stadistics = Response(**jts)
        assert jts["success"] == team_stadistics.success
