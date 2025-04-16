"""
Standings
"""


class Standing:
    place: str
    player: str
    player_key: str
    league: str
    movement: str
    country: str
    points: str

    def __init__(
        self,
        place: str,
        player: str,
        player_key: str,
        league: str,
        movement: str,
        country: str,
        points: str,
    ):
        """
        Constructor.
        """
        self.place = place
        self.player = player
        self.player_key = player_key
        self.league = league
        self.movement = movement
        self.country = country
        self.points = points
        self.__dict__ = globals()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__

    def __iter__(self):
        yield "place", self.place
        yield "player", self.player
        yield "player_key", self.player_key
        yield "league", self.league
        yield "movement", self.movement
        yield "country", self.country
        yield "points", self.points
