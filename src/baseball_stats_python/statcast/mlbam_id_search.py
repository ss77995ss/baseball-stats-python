import logging

import pandas as pd

from ..utils.fetch import fetch_json
from ..utils.log import enable_debug_logging

logger = logging.getLogger(__name__)


MLBAM_ID_SEARCH_URL = 'https://baseballsavant.mlb.com/player/search-all'


def mlbam_id_search(
    player_name: str, limit: int | None = 10, debug: bool = False
) -> pd.DataFrame:
    """
    Search for MLBAM ID(s) by player's name.

    Args:
        player_name (str): The player name to search for. (Required)
        limit (int | None): Return at most this many of the most relevant results. None returns all.
        debug (bool): Whether to print debug information.

    Returns:
        pd.DataFrame: A DataFrame containing the MLBAM ID(s).
    """

    if not player_name:
        raise ValueError('player_name is required')

    if debug:
        enable_debug_logging()

    result = pd.DataFrame(
        fetch_json(
            MLBAM_ID_SEARCH_URL,
            {'search': player_name},
            source='MLBAM ID search',
        )
    )
    logger.debug(result)

    if limit is not None and len(result) > limit:
        logger.info(
            'Showing the %d most relevant of %d results', limit, len(result)
        )
        return result.head(limit)
    return result
