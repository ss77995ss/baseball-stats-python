import pandas as pd
import requests

from ..constants import DEFAULT_SEASON
from ..enums.statcast_leaderboard import GameType

session = requests.Session()

API_URL = 'https://baseballsavant.mlb.com/leaderboard/services/baserunning'


def runner_extra_bases_taken(
    runner_id: str,
    game_type: str | GameType = GameType.REGULAR_SEASON,
    season: str = str(DEFAULT_SEASON),
) -> pd.DataFrame:
    """
    Get extra base taken data from each advanced opportunity for a specific runner.
    ref: https://baseballsavant.mlb.com/leaderboard/baserunning

    Args:
        runner_id (str): The MLBAM ID of the runner. (Required)
        game_type (str | GameType): The game type to filter by. Default is "Regular".
        season (str): The season to filter by. The earliest season available is 2016.
    Returns:
        pd.DataFrame: A DataFrame containing the baserunning data.
    """

    if not runner_id:
        raise ValueError('runner_id is required')

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

    response = session.get(f'{API_URL}/{runner_id}', params=params)

    if response.status_code == 200:
        result = response.json()
        df = pd.DataFrame(result['data'])
        return df
    else:
        raise Exception(
            f'Failed to fetch data: {response.status_code} - {response.text}'
        )
