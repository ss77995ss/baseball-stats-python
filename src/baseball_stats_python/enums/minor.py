from .enum_base import EnumBase


class MinorGameType(EnumBase):
    """
    Enum for Minor League Game Types.
    Currently Minor League Statcast Search only supports Regular Season and Playoffs.

    REGULAR_SEASON = "R",
    PLAYOFFS = "PO"
    """

    REGULAR_SEASON = 'R'
    PLAYOFFS = 'PO'


class Level(EnumBase):
    """
    Enum for Minor League Levels.
    Currently Minor League Statcast Search only supports A and AAA.

    A - Single-A\n
    AAA - Triple-A
    """

    A = 'A'
    AAA = 'AAA'
