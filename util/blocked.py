from enum import Enum, auto


class Blocked(Enum):
    DEAD_END = auto()
    ROCK_SMASH = auto()
    STRENGTH = auto()
    SURF = auto()
    WATERFALL = auto()
    TRAINER = auto()
    EVENT = auto()

