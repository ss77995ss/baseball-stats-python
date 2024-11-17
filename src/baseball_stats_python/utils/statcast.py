from ..constants import DEFAULT_SEASON
from ..enums.statcast import GameType, MlbTeam, Month

START_SEASON = 2008
STATCAST_START_SEASON = 2015

ALL_SEASONS = [str(year) for year in range(START_SEASON, DEFAULT_SEASON + 1)]
STATCAST_SEASONS = [
    str(year) for year in range(STATCAST_START_SEASON, DEFAULT_SEASON + 1)
]


def get_season_param_str(season: str | list[str]) -> str:
    if not isinstance(season, str) and not isinstance(season, list):
        raise ValueError(f'Invalid type for season: {type(season)}')

    if isinstance(season, list):
        if any(season not in ALL_SEASONS for season in season):
            raise ValueError(f'Invalid seasons: {season}')
        return '|'.join(season)

    if season == '':
        return str(DEFAULT_SEASON)
    if season == 'all':
        return '|'.join(ALL_SEASONS)
    if season == 'statcast':
        return '|'.join(STATCAST_SEASONS)

    if season not in ALL_SEASONS:
        raise ValueError(f'Invalid season: {season}')

    return season


def get_game_type_param_str(game_type: str | GameType | list[str | GameType]) -> str:
    if (
        not isinstance(game_type, str)
        and not isinstance(game_type, list)
        and not isinstance(game_type, GameType)
    ):
        raise ValueError(f'Invalid type for game_type: {type(game_type)}')

    if isinstance(game_type, list):
        str_game_type = [str(game_type) for game_type in game_type]
        if any(not GameType.has_value(game_type) for game_type in str_game_type):
            raise ValueError(f"Invalid game types: {'|'.join(str_game_type)}")
        return f"{'|'.join(str_game_type)}|"

    if game_type == '':
        return 'R|'

    if game_type == 'all':
        return f'{GameType.join_all()}|'

    if not GameType.has_value(game_type):
        raise ValueError(f'Invalid game type: {game_type}')

    return f'{game_type}|'


def get_month_param_str(month: str | Month | list[str | Month]) -> str:
    if (
        not isinstance(month, str)
        and not isinstance(month, list)
        and not isinstance(month, Month)
    ):
        raise ValueError(f'Invalid type for month: {type(month)}')

    if isinstance(month, list):
        str_month = [str(month) for month in month]
        if any(not Month.has_value(month) for month in str_month):
            raise ValueError(f"Invalid months: {'|'.join(str_month)}")
        return f"{'|'.join(str_month)}|"

    if month == '':
        return ''

    if month == 'all':
        return f'{Month.join_all()}|'

    if not Month.has_value(month):
        raise ValueError(f'Invalid month: {month}')

    return f'{month}|'


def get_team_param_str(team: str | MlbTeam | list[str | MlbTeam]) -> str:
    if (
        not isinstance(team, str)
        and not isinstance(team, list)
        and not isinstance(team, MlbTeam)
    ):
        raise ValueError(f'Invalid type for team: {type(team)}')

    if isinstance(team, list):
        str_team = [str(team) for team in team]
        if any(not MlbTeam.has_value(team) for team in str_team):
            raise ValueError(f"Invalid teams: {'|'.join(str_team)}")
        return f"{'|'.join(str_team)}|"

    if team == '':
        return ''

    if team == 'all':
        return f'{MlbTeam.join_all()}|'

    if not MlbTeam.has_value(team):
        raise ValueError(f'Invalid team: {team}')

    return f'{team}|'
