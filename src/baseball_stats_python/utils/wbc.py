from ..constants import DEFAULT_SEASON
from ..enums.wbc import WbcGameType

# TODO: Remove 2025 once Baseball Savant changes their default season
ALL_SEASONS = ["2023", "2026"]


def get_wbc_season_param_str(season: str | list[str]) -> str:
    if not isinstance(season, str) and not isinstance(season, list):
        raise ValueError(f"Invalid type for season: {type(season)}")

    if isinstance(season, list):
        if any(season not in ALL_SEASONS for season in season):
            raise ValueError(f"Invalid seasons: {season}")
        return "|".join(season)

    if season == "":
        return str(DEFAULT_SEASON)
    if season == "all":
        return "|".join(ALL_SEASONS)

    if season not in ALL_SEASONS:
        raise ValueError(f"Invalid season: {season}")

    return season


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
