import pandas as pd

from ..constants import DEFAULT_SEASON
from ..enums.statcast_leaderboard import GameType
from ..utils.fetch import fetch_json

API_URL = 'https://baseballsavant.mlb.com/leaderboard/services/baserunning'


def runner_extra_bases_taken(
    runner_id: str,
    game_type: str | GameType = GameType.REGULAR_SEASON,
    season: int | str = DEFAULT_SEASON,
) -> pd.DataFrame:
    """
    Get extra base taken data from each advanced opportunity for a specific runner.
    ref: https://baseballsavant.mlb.com/leaderboard/baserunning

    Args:
        runner_id (str): The MLBAM ID of the runner. (Required)
        game_type (str | GameType): The game type to filter by. Default is "Regular".
        season (int | str): The season to filter by. The earliest season available is 2016.
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

    result = fetch_json(f'{API_URL}/{runner_id}', params, source='Runner extra bases taken')
    df = pd.DataFrame(result['data'])
    return df
