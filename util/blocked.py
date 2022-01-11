from enum import Enum, auto


class Blocked(Enum):
    DEAD_END = auto()
    CUT = auto()
    ROCK_SMASH = auto()
    STRENGTH = auto()
    SURF = auto()
    WATERFALL = auto()
    ROCK_CLIMB = auto()
    TRAINER = auto()
    EVENT = auto()

