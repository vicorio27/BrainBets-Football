"""
Match Object
"""

from models.team_match_stat import TeamMatch


class Match:
    local_team: TeamMatch
    away_team: TeamMatch
    # exmp: 1 - 0 or 0 - 1
    result: str

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
