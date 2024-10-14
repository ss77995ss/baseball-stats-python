from ..enums.minor import MinorGameType, Level


CURRENT_SEASON = 2024
START_SEASON = 2021

ALL_SEASONS = [str(year) for year in range(START_SEASON, CURRENT_SEASON + 1)]


def get_minor_season_param_str(season: str | list[str]) -> str:
    if (type(season) != str and type(season) != list):
        raise ValueError(f"Invalid type for season: {type(season)}")

    if (type(season) == list):
        if any(season not in ALL_SEASONS for season in season):
            raise ValueError(f"Invalid seasons: {season}")
        return '|'.join(season)

    if (season == ""):
        return str(CURRENT_SEASON)
    if (season == "all"):
        return '|'.join(ALL_SEASONS)

    if (season not in ALL_SEASONS):
        raise ValueError(f"Invalid season: {season}")

    return season


def get_minor_game_type_param_str(game_type: str | MinorGameType | list[str | MinorGameType]) -> str:
    if (type(game_type) != str and type(game_type) != list and not isinstance(game_type, MinorGameType)):
        raise ValueError(f"Invalid type for game_type: {type(game_type)}")

    if (type(game_type) == list):
        str_game_type = [str(game_type) for game_type in game_type]
        if any(not MinorGameType.has_value(game_type) for game_type in str_game_type):
            raise ValueError(f"Invalid game types: {'|'.join(str_game_type)}")
        return f"{'|'.join(str_game_type)}|"

    if (game_type == ""):
        return "R|"

    if (game_type == "all"):
        return f"{MinorGameType.join_all()}|"

    if (not MinorGameType.has_value(game_type)):
        raise ValueError(f"Invalid game type: {game_type}")

    return f"{game_type}|"


def get_level_param_str(level: str | Level | list[str | Level]) -> str:
    if (type(level) != str and type(level) != list and not isinstance(level, MinorGameType)):
        raise ValueError(f"Invalid type for level: {type(level)}")

    if (type(level) == list):
        str_level = [str(level) for level in level]
        if any(not MinorGameType.has_value(level) for level in str_level):
            raise ValueError(f"Invalid levels: {'|'.join(str_level)}")
        return f"{'|'.join(str_level)}|"

    if (level == ""):
        return ""

    if (level == "all"):
        return f"{MinorGameType.join_all()}|"

    if (not MinorGameType.has_value(level)):
        raise ValueError(f"Invalid level: {level}")

    return f"{level}|"
