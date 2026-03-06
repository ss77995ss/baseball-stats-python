import io
import logging

import pandas as pd
import requests

from ..enums.wbc import WbcGameType
from ..utils.wbc import get_wbc_game_type_param_str, get_wbc_season_param_str

logging.basicConfig()
logger = logging.getLogger()

session = requests.Session()


WBC_STATCAST_SEARCH_URL = (
    "https://baseballsavant.mlb.com/statcast-search-world-baseball-classic/csv"
)


def wbc_statcast_search(
    season: str | list[str] = "2026",
    player_type: str = "pitcher",
    game_type: str | WbcGameType | list[str | WbcGameType] = "",
    pitchers_lookup: str | list[str] = "",
    batters_lookup: str | list[str] = "",
    debug: bool = False,
) -> pd.DataFrame:
    """
    Search for WBC Statcast pitch-level data with custom filters.

    Args:
        season (str | list[str]): The season(s) to search for.
        player_type (str): The type of player to search for.
        pitchers_lookup (str | list[str]): The pitcher(s) to search for.
        batters_lookup (str | list[str]): The batter(s) to search for.

    Returns:
        pd.DataFrame: A DataFrame containing the WBC Statcast pitch-level data.
    """

    if debug:
        logger.setLevel(logging.DEBUG)

    params = {
        "all": "true",
        "player_type": player_type,
        "hfSea": get_wbc_season_param_str(season),
        "hfGT": get_wbc_game_type_param_str(game_type),
        "type": "details",
        "wbc": "true",
    }

    if pitchers_lookup:
        params["pitchers_lookup[]"] = pitchers_lookup

    if batters_lookup:
        params["batters_lookup[]"] = batters_lookup

    logger.debug(f"Params: {params}")

    print("Starting WBC Statcast Search")
    response = session.get(WBC_STATCAST_SEARCH_URL, params=params)

    logger.debug(response.url)

    if response.status_code == 200:
        print("WBC Statcast Search Completed")
        csv_content = io.StringIO(response.text)

        return pd.read_csv(csv_content)
    else:
        raise Exception(
            f"Failed to fetch data: {response.status_code} - {response.text}"
        )


def wbc_statcast_pitcher_search(
    pitchers_lookup: str | list[str],
    season: str | list[str] = "2026",
    game_type: str | WbcGameType | list[str | WbcGameType] = "",
    debug: bool = False,
) -> pd.DataFrame:
    """
    Search for WBC Statcast pitch-level data for pitcher(s) with custom filters.
    Args:
        pitchers_lookup (str | list[str]): The pitcher(s) to search for. (Required)
        season (str | list[str]): The season(s) to search for.
        game_type (str | WbcGameType | list[str | WbcGameType]): The game type(s) to search for.
    Returns:
        pd.DataFrame: A DataFrame containing the WBC Statcast pitch-level data for target pitcher(s).
    """

    if not pitchers_lookup:
        raise ValueError("pitchers_lookup is required")

    params = {
        "pitchers_lookup": pitchers_lookup,
        "season": season,
        "player_type": "pitcher",
        "game_type": game_type,
        "debug": debug,
    }

    return wbc_statcast_search(**params)


def wbc_statcast_batter_search(
    batters_lookup: str | list[str],
    season: str | list[str] = "2026",
    game_type: str | WbcGameType | list[str | WbcGameType] = "",
    debug: bool = False,
) -> pd.DataFrame:
    """
    Search for WBC Statcast pitch-level data for batter(s) with custom filters.
    Args:
        batters_lookup (str | list[str]): The batter(s) to search for. (Required)
        season (str | list[str]): The season(s) to search for.
        game_type (str | WbcGameType | list[str | WbcGameType]): The game type(s) to search for.
    Returns:
        pd.DataFrame: A DataFrame containing the WBC Statcast pitch-level data for target batter(s).
    """

    if not batters_lookup:
        raise ValueError("batters_lookup is required")

    params = {
        "batters_lookup": batters_lookup,
        "season": season,
        "player_type": "batter",
        "game_type": game_type,
        "debug": debug,
    }

    return wbc_statcast_search(**params)
