import pandas as pd
import requests

from ..constants import DEFAULT_SEASON
from ..enums.statcast_leaderboard import GameType

session = requests.Session()

API_URL = 'https://baseballsavant.mlb.com/leaderboard/services/catcher-throwing'


def catcher_throwing(
    catcher_id: str,
    game_type: str | GameType = GameType.REGULAR_SEASON,
    season: str = str(DEFAULT_SEASON),
) -> pd.DataFrame:
    """
    Get catcher throwing data from each stolen base attempt for a specific catcher.
    ref: https://baseballsavant.mlb.com/leaderboard/catcher-throwing

    Args:
        catcher_id (str): The MLBAM ID of the catcher. (Required)
        game_type (str): The game type to filter by.
        n (str): The number of results to return.
        season (str): The season to filter by. The earliest season available is 2016.

    Returns:
        pd.DataFrame: A DataFrame containing the catcher throwing data.
    """

    if not catcher_id:
        raise ValueError('catcher_id is required')

    if not isinstance(game_type, str) and not isinstance(game_type, GameType):
        raise ValueError(f'Invalid type for game_type: {type(game_type)}')

    if not GameType.has_value(game_type):
        raise ValueError(f'Invalid game type: {game_type}')

    if int(season) < 2016:
        raise ValueError(
            f'Invalid season: {season}, The earliest season available is 2016'
        )

    params = {
        'game_type': game_type,
        'season_start': season,
        'season_end': season,
        'n': 0,
    }

    response = session.get(f'{API_URL}/{catcher_id}', params=params)

    if response.status_code == 200:
        result = response.json()
        return pd.DataFrame(result['data'])
    else:
        raise Exception(
            f'Failed to fetch data: {response.status_code} - {response.text}'
        )
