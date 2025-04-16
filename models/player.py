"""
Stats
"""


class Stats:
    season: str
    type: str
    rank: str
    titles: str
    matches_won: str
    matches_lost: str
    hard_won: str
    hard_lost: str
    clay_won: str
    clay_lost: str
    grass_won: str
    grass_lost: str

    def __init__(
        self,
        season: str,
        type: str,
        rank: str,
        titles: str,
        matches_won: str,
        matches_lost: str,
        hard_won: str,
        hard_lost: str,
        clay_won: str,
        clay_lost: str,
        grass_won: str,
        grass_lost: str,
    ):
        """
        Constructor.
        """
        self.season = season
        self.type = type
        self.rank = rank
        self.titles = titles
        self.matches_won = matches_won
        self.matches_lost = matches_lost
        self.hard_won = hard_won
        self.hard_lost = hard_lost
        self.clay_won = clay_won
        self.clay_lost = clay_lost
        self.grass_won = grass_won
        self.grass_lost = grass_lost
        self.__dict__ = globals()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__

    def __iter__(self):
        yield "season", self.season
        yield "type", self.type
        yield "rank", self.rank
        yield "titles", self.titles
        yield "matches_won", self.matches_won
        yield "matches_lost", self.matches_lost
        yield "hard_won", self.hard_won
        yield "hard_lost", self.hard_lost
        yield "clay_won", self.clay_won
        yield "clay_lost", self.clay_lost
        yield "grass_won", self.grass_won
        yield "grass_lost", self.grass_lost


"""
Player
"""


class Player:
    player_key: str
    player_name: str
    player_country: str
    player_bday: str
    player_logo: str
    stats: list[Stats]

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
