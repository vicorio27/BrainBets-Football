"""
Point
"""


class Point:
    number_point: str
    score: str
    break_point: str
    set_point: str
    match_point: str

    def __init__(
        self,
        number_point: str,
        score: str,
        break_point: str,
        set_point: str,
        match_point: str,
    ):
        """
        Constructor.
        """
        self.number_point = number_point
        self.score = score
        self.break_point = break_point
        self.set_point = set_point
        self.match_point = match_point
        self.__dict__ = globals()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__

    def __iter__(self):
        yield "number_point", self.number_point
        yield "score", self.score
        yield "break_point", self.break_point
        yield "set_point", self.set_point
        yield "match_point", self.match_point


"""
PointByPoint
"""


class PointByPoint:
    set_number: str
    number_game: str
    player_served: str
    serve_winner: str
    serve_lost: str
    score: str
    points: list[Point]

    def __init__(
        self,
        set_number: str,
        number_game: str,
        player_served: str,
        serve_winner: str,
        serve_lost: str,
        score: str,
        points: list[Point],
    ):
        """
        Constructor.
        """
        self.set_number = set_number
        self.number_game = number_game
        self.player_served = player_served
        self.serve_winner = serve_winner
        self.serve_lost = serve_lost
        self.score = score
        self.points = points
        self.__dict__ = globals()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__

    def __iter__(self):
        yield "set_number", self.set_number
        yield "number_game", self.number_game
        yield "player_served", self.player_served
        yield "serve_winner", self.serve_winner
        yield "serve_lost", self.serve_lost
        yield "score", self.score
        yield "points", self.points


"""
Score
"""


class Score:
    score_first: str
    score_second: str
    score_set: str

    def __init__(self, score_first: str, score_second: str, score_set: str):
        """
        Constructor.
        """
        self.score_first = score_first
        self.score_second = score_second
        self.score_set = score_set
        self.__dict__ = globals()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__

    def __iter__(self):
        yield "score_first", self.score_first
        yield "score_second", self.score_second
        yield "score_set", self.score_set


"""
Fixtures
"""


class Fixtures:
    event_key: str
    event_date: str
    event_time: str
    event_first_player: str
    first_player_key: str
    event_second_player: str
    second_player_key: str
    event_final_result: str
    event_game_result: str
    event_serve: str
    event_winner: str
    event_status: str
    event_type_type: str
    tournament_name: str
    tournament_key: str
    tournament_round: str
    tournament_season: str
    event_live: str
    event_qualification: str
    event_first_player_logo: str
    event_second_player_logo: str
    pointbypoint: list[PointByPoint]
    scores: list[Score]

    def __init__(self, event_type_key: str, event_type_type: str):
        """
        Constructor.
        """
        self.event_type_key = event_type_key
        self.event_type_type = event_type_type
        self.__dict__ = globals()

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__

    def __iter__(self):
        yield "event_type_key", self.event_type_key
        yield "event_type_type", self.event_type_type
