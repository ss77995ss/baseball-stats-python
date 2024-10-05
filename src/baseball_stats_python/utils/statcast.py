CURRENT_SEASON = 2024
START_SEASON = 2008
STATCAST_START_SEASON = 2015

ALL_SEASONS = [str(year) for year in range(START_SEASON, CURRENT_SEASON)]
STATCAST_SEASONS = [str(year) for year in range(
    STATCAST_START_SEASON, CURRENT_SEASON)]


def get_season_param_str(season: str | list[str]) -> str:
    if (type(season) != str and type(season) != list):
        raise ValueError(f"Invalid type for season: {season}")

    if (type(season) == list):
        if any(season not in ALL_SEASONS for season in season):
            raise ValueError(f"Invalid seasons: {" | ".join(season)}")
        return '|'.join(season)

    if (season == "all"):
        return '|'.join(ALL_SEASONS)
    if (season == "statcast"):
        return '|'.join(STATCAST_SEASONS)

    if (season not in ALL_SEASONS):
        raise ValueError(f"Invalid season: {season}")

    return season


GAME_TYPES = ["R", "PO", "F", "D", "L", "W", "S", "A"]


def get_game_type_param_str(game_type: str | list[str]) -> str:
    if (type(game_type) != str and type(game_type) != list):
        raise ValueError(f"Invalid type for game_type: {game_type}")

    if (type(game_type) == list):
        if any(game_type not in GAME_TYPES for game_type in game_type):
            raise ValueError(f"Invalid game types: {" | ".join(game_type)}")
        return f"{'|'.join(game_type)}|"

    if (game_type == "all"):
        return f"{'|'.join(GAME_TYPES)}|"

    if (game_type not in GAME_TYPES):
        raise ValueError(f"Invalid game type: {game_type}")

    return f"{game_type}|"
