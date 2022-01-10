from enum import Enum


class Blocked(Enum):
    DEAD_END = 0
    CUT = 1
    ROCK_SMASH = 2
    STRENGTH = 3
    SURF = 4
    ROCK_CLIMB = 5
    WATERFALL = 6
    TRAINER = 7
    EVENT = 8

