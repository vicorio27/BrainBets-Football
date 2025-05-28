"""
MatchOverView
"""

from models.team_overview import TeamOverview
from models.match import Match


class MatchOverview:
    team1_stats: TeamOverview
    team1_last_matches: list[Match]
    team1_last_tournament_matches: list[Match]

    team2_stats: TeamOverview
    team2_last_matches: list[Match]
    team2_last_tournament_matches: list[Match]

    team1_and_team2_last_matches_between_them: list[Match]

    def __init__(self, **kwargs):
        """
        Constructor.
        """
        self.__dict__.update(kwargs)
        self.__dict__ = globals()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__
