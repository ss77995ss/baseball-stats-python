import io
import logging

import pandas as pd
import requests

from ..enums.statcast import GameType, MlbTeam, Month
from ..utils.statcast import (
    get_game_type_param_str,
    get_month_param_str,
    get_season_param_str,
    get_team_param_str,
)
from ..utils.utils import validate_date_range

logging.basicConfig()
logger = logging.getLogger('Statcast')

session = requests.Session()

STATCAST_SEARCH_URL = 'https://baseballsavant.mlb.com/statcast_search/csv'


def statcast_search(
    season: str | list[str] = '2024',
    player_type: str = 'pitcher',
    game_type: str | GameType | list[str | GameType] = GameType.REGULAR_SEASON,
    start_dt: str = '',
    end_dt: str = '',
    month: str | Month | list[str | Month] = '',
    pitchers_lookup: str | list[str] = '',
    batters_lookup: str | list[str] = '',
    team: str | MlbTeam | list[str | MlbTeam] = '',
    opponent: str | MlbTeam | list[str | MlbTeam] = '',
    debug: bool = False,
) -> pd.DataFrame:
    """
    Search for Statcast pitch-level data with custom filters.

    Args:
        season (str | list[str]): The season(s) to search for.
        player_type (str): The type of player to search for.
        game_type (str | GameType | list[str | GameType]): The game type(s) to search for.
        start_dt (str): The start date in 'YYYY-MM-DD' format.
        end_dt (str): The end date in 'YYYY-MM-DD' format.
        month (str | Month | list[str | Month]): The month(s) to search for.
        pitchers_lookup (str | list[str]): The pitcher(s) to search for.
        batters_lookup (str | list[str]): The batter(s) to search for.
        team (str | MlbTeam | list[str | MlbTeam]): The team(s) to search for.
        opponent (str | MlbTeam | list[str | MlbTeam]): The opponent(s) to search for.

    Returns:
        pd.DataFrame: A DataFrame containing the Statcast pitch-level data.
    """

    if debug:
        logger.setLevel(logging.DEBUG)

    if start_dt or end_dt:
        validate_date_range(start_dt, end_dt)

    params = {
        'all': 'true',
        'player_type': player_type,
        'hfSea': get_season_param_str(season),
        'hfGT': get_game_type_param_str(game_type),
        'game_date_gt': start_dt,
        'game_date_lt': end_dt,
        'hfMo': get_month_param_str(month),
        'hfTeam': get_team_param_str(team),
        'hfOpponent': get_team_param_str(opponent),
        'type': 'details',
    }

    if pitchers_lookup:
        params['pitchers_lookup[]'] = pitchers_lookup

    if batters_lookup:
        params['batters_lookup[]'] = batters_lookup

    print('Starting Statcast Search')
    logger.debug(f'Params: {params}')
    response = session.get(STATCAST_SEARCH_URL, params=params)

    logger.debug(response.url)

    if response.status_code == 200:
        print('Statcast Search Completed')
        csv_content = io.StringIO(response.text)

        return pd.read_csv(csv_content)
    else:
        raise Exception(
            f'Failed to fetch data: {response.status_code} - {response.text}'
        )


def statcast_pitcher_search(
    pitchers_lookup: str | list[str],
    season: str | list[str] = '2024',
    game_type: str | GameType | list[str | GameType] = GameType.REGULAR_SEASON,
    start_dt: str = '',
    end_dt: str = '',
    month: str | Month | list[str | Month] = '',
    opponent: str | MlbTeam | list[str | MlbTeam] = '',
    debug: bool = False,
) -> pd.DataFrame:
    """
    Search for Statcast pitch-level data for pitcher(s) with custom filters.

    Args:
        pitchers_lookup (str | list[str]): The pitcher(s) to search for. (Required)
        season (str | list[str]): The season(s) to search for.
        game_type (str | GameType | list[str | GameType]): The game type(s) to search for.
        start_dt (str): The start date in 'YYYY-MM-DD' format.
        end_dt (str): The end date in 'YYYY-MM-DD' format.
        month (str | Month | list[str | Month]): The month(s) to search for.
        opponent (str | MlbTeam | list[str | MlbTeam]): The opponent(s) to search for.

    Returns:
        pd.DataFrame: A DataFrame containing the Statcast pitch-level data for target pitcher(s).
    """

    if not pitchers_lookup:
        raise ValueError('pitchers_lookup is required')

    params = {
        'pitchers_lookup': pitchers_lookup,
        'season': season,
        'player_type': 'pitcher',
        'game_type': game_type,
        'start_dt': start_dt,
        'end_dt': end_dt,
        'month': month,
        'opponent': opponent,
        'debug': debug,
    }

    return statcast_search(**params)


def statcast_batter_search(
    batters_lookup: str | list[str],
    season: str | list[str] = '2024',
    game_type: str | GameType | list[str | GameType] = GameType.REGULAR_SEASON,
    start_dt: str = '',
    end_dt: str = '',
    month: str | Month | list[str | Month] = '',
    opponent: str | MlbTeam | list[str | MlbTeam] = '',
    debug: bool = False,
) -> pd.DataFrame:
    """
    Search for Statcast pitch-level data for batter(s) with custom filters.

    Args:
        batters_lookup (str | list[str]): The batter(s) to search for. (Required)
        season (str | list[str]): The season(s) to search for.
        game_type (str | GameType | list[str | GameType]): The game type(s) to search for.
        start_dt (str): The start date in 'YYYY-MM-DD' format.
        end_dt (str): The end date in 'YYYY-MM-DD' format.
        month (str | Month | list[str | Month]): The month(s) to search for.
        opponent (str | MlbTeam | list[str | MlbTeam]): The opponent(s) to search for.

    Returns:
        pd.DataFrame: A DataFrame containing the Statcast pitch-level data for target batter(s).
    """

    if not batters_lookup:
        raise ValueError('batters_lookup is required')

    params = {
        'batters_lookup': batters_lookup,
        'season': season,
        'player_type': 'batter',
        'game_type': game_type,
        'start_dt': start_dt,
        'end_dt': end_dt,
        'month': month,
        'opponent': opponent,
        'debug': debug,
    }

    return statcast_search(**params)
