from event import Event

"""
Tournament
"""


class Tournament:
    tournament_key: str
    tournament_name: str
    event: Event

    def __init__(self, tournament_key: str, tournament_name: str, event: Event):
        """
        Constructor.
        """
        self.event_type_key = tournament_key
        self.event_type_type = tournament_name
        self.event = event
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
        yield "event", self.event.serialize()
