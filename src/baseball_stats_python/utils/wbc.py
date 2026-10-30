from ..enums.wbc import WbcGameType
from .seasons import SeasonInput, build_season_param

# The WBC is not played every year; add new editions here.
ALL_SEASONS = ["2023", "2026"]


def get_wbc_season_param_str(season: SeasonInput) -> str:
    return build_season_param(
        season,
        ALL_SEASONS,
        aliases={"all": ALL_SEASONS},
        default=ALL_SEASONS[-1],
    )


def get_wbc_game_type_param_str(
    game_type: str | WbcGameType | list[str | WbcGameType],
) -> str:
    if (
        not isinstance(game_type, str)
        and not isinstance(game_type, list)
        and not isinstance(game_type, WbcGameType)
    ):
        raise ValueError(f"Invalid type for game_type: {type(game_type)}")

    if isinstance(game_type, list):
        str_game_type = [str(game_type) for game_type in game_type]
        if any(not WbcGameType.has_value(game_type) for game_type in str_game_type):
            raise ValueError(f"Invalid game types: {'|'.join(str_game_type)}")
        return f"{'|'.join(str_game_type)}|"

    if game_type == "":
        return "F|CL|CD|CW|"

    if game_type == "all":
        return f"{WbcGameType.join_all()}|"

    if not WbcGameType.has_value(game_type):
        raise ValueError(f"Invalid game type: {game_type}")

    return f"{game_type}|"
