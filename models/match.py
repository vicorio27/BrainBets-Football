"""
Match Object
"""

class Match:
    local_team: str
    local_goals: int
    local_assists: int
    local_corners: int
    local_yellow_card: int
    local_red_card: int
    local_shoot: int
    local_on_target_shoot: int

    away_goal: int
    away_assists: int
    away_corners: int
    away_yellow_card: int
    away_red_card: int
    away_shoot: int
    away_on_target_shoot: int


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
