import pandas as pd
import requests

from ..constants import DEFAULT_SEASON
from ..enums.statcast_leaderboard import GameType, Hand
from ..utils.statcast_leaderboard import get_hand_param_str, get_prior_pk_param_str

session = requests.Session()

API_URL = (
    'https://baseballsavant.mlb.com/leaderboard/services/basestealing-running-game'
)


def get_run_value(df: pd.DataFrame) -> float:
    if df['is_runner_cs']:
        return -0.45
    if df['is_runner_sb']:
        return 0.2
    if df['is_runner_pk']:
        return -0.45
    if df['is_runner_bk']:
        return 0.2
    if df['is_runner_fb']:
        return 0.2

    raise ValueError(f'Invalid DataFrame: {df}')


def runner_basestealing(
    runner_id: str,
    game_type: str | GameType = GameType.REGULAR_SEASON,
    season: str = str(DEFAULT_SEASON),
    pitch_hand: str | Hand = Hand.ALL,
    prior_pk: str = 'all',
) -> pd.DataFrame:
    """
    Get basestealing data from each stolen base opportunity for a specific runner.
    ref: https://baseballsavant.mlb.com/leaderboard/basestealing-run-value

    Args:
        runner_id (str): The MLBAM ID of the runner. (Required)
        game_type (str | GameType): The game type to filter by. Default is "Regular".
        season (str): The season to filter by. The earliest season available is 2016.
        pitch_hand (str | Hand): The pitch hand to filter by. Default is "all".
        prior_pk (str): The number of prior pick-off attempts from pitcher before the stolen base opportunity. Default is "all".
                        Can be "all", "1", "2", or "3". "3" is include all prior pick-off attempts over 3.
    Returns:
        pd.DataFrame: A DataFrame containing the basestealing data.
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
        'pitch_hand': get_hand_param_str(pitch_hand),
        'prior_pk': get_prior_pk_param_str(prior_pk),
    }

    response = session.get(f'{API_URL}/{runner_id}', params=params)

    if response.status_code == 200:
        result = response.json()
        df = pd.DataFrame(result['data'])
        df['run_value'] = df.apply(get_run_value, axis=1)
        return df
    else:
        raise Exception(
            f'Failed to fetch data: {response.status_code} - {response.text}'
        )
