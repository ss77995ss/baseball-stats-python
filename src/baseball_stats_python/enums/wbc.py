from .enum_base import EnumBase


class WbcGameType(EnumBase):
    """
    Enum for WBC Game Types.
    Currently WBC Statcast Search only supports Pool Play, Semi-Finals, Quarter-Finals, and Championship.

    POOL_PLAY = "F",
    SEMI_FINALS = "CL",
    QUARTER_FINALS = "CD",
    CHAMPIONSHIP = "CW"
    """

    POOL_PLAY = "F"
    SEMI_FINALS = "CL"
    QUARTER_FINALS = "CD"
    CHAMPIONSHIP = "CW"
