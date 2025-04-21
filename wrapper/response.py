from dataclasses import dataclass

"""
Response Wrapper class
"""

@dataclass
class Response:

    success: int
    result: list[any]

    def __init__(self, **kwargs):
        """
        Constructor.
        """
        self.__dict__.update(kwargs)

    def __str__(self):
        return self.__class__.__name__

    def __hash__(self):
        return hash((self.__class__.__name__))

    def serialize(self):
        return self.__dict__
