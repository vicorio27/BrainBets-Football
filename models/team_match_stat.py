"""
TeamMatch Object
"""


class TeamMatch:
    name: str
    goals: int
    assists: int
    corners: int
    """
    "cards": {
		  "red": 3,
		  "yellow": 2,
	    }
    """
    cards: dict
    shoot: int
    on_target_shoot: int

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
