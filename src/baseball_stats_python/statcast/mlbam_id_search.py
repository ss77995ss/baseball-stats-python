import logging

import pandas as pd
import requests

logger = logging.getLogger()

session = requests.Session()

MLBAM_ID_SEARCH_URL = 'https://baseballsavant.mlb.com/player/search-all'


def mlbam_id_search(player_name: str, debug: bool = False) -> pd.DataFrame:
    """
    Search for MLBAM ID(s) by player name.

    Args:
        player_name (str): The player name to search for. (Required)
        debug (bool): Whether to print debug information.

    Returns:
        pd.DataFrame: A DataFrame containing the MLBAM ID(s).
    """

    if not player_name:
        raise ValueError('player_name is required')

    if debug:
        logger.setLevel(logging.DEBUG)

    print('Starting MLBAM ID Search')
    response = session.get(MLBAM_ID_SEARCH_URL, params={'search': player_name})

    if response.status_code == 200:
        print('MLBAM ID Search Completed')
        result = pd.DataFrame(response.json())

        logger.debug(result)

        if len(result) > 10:
            print('Only showing first 10 most relevant results')

            return result.head(10)
        else:
            return result

    else:
        raise Exception(
            f'Failed to fetch data: {response.status_code} - {response.text}'
        )
