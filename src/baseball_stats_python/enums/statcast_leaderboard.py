from .enum_base import EnumBase


class GameType(EnumBase):
    REGULAR_SEASON = 'Regular'
    PLAYOFFS = 'Playoff'
    ALL = 'All'


class Hand(EnumBase):
    RIGHT = 'R'
    LEFT = 'L'
    ALL = 'all'
