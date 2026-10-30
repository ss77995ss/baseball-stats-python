import logging

import pandas as pd

from ..constants import DEFAULT_SEASON
from ..enums.statcast import GameType, MlbTeam, Month
from ..utils.fetch import fetch_csv
from ..utils.log import enable_debug_logging
from ..utils.seasons import SeasonInput
from ..utils.statcast import (
    get_game_type_param_str,
    get_month_param_str,
    get_season_param_str,
    get_team_param_str,
)
from ..utils.utils import validate_date_range

logger = logging.getLogger(__name__)


STATCAST_SEARCH_URL = "https://baseballsavant.mlb.com/statcast_search/csv"


def statcast_search(
    season: SeasonInput = DEFAULT_SEASON,
    player_type: str = "pitcher",
    game_type: str | GameType | list[str | GameType] = GameType.REGULAR_SEASON,
    start_dt: str = "",
    end_dt: str = "",
    month: str | Month | list[str | Month] = "",
    pitchers_lookup: str | list[str] = "",
    batters_lookup: str | list[str] = "",
    team: str | MlbTeam | list[str | MlbTeam] = "",
    opponent: str | MlbTeam | list[str | MlbTeam] = "",
    debug: bool = False,
) -> pd.DataFrame:
    """
    Search for Statcast pitch-level data with custom filters.

    Args:
        season (int | str | list[int | str]): The season(s) to search for. Defaults to the current season.
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
        enable_debug_logging()

    if start_dt or end_dt:
        validate_date_range(start_dt, end_dt)

    params = {
        "all": "true",
        "player_type": player_type,
        "hfSea": get_season_param_str(season),
        "hfGT": get_game_type_param_str(game_type),
        "game_date_gt": start_dt,
        "game_date_lt": end_dt,
        "hfMo": get_month_param_str(month),
        "hfTeam": get_team_param_str(team),
        "hfOpponent": get_team_param_str(opponent),
        "type": "details",
    }

    if pitchers_lookup:
        params["pitchers_lookup[]"] = pitchers_lookup

    if batters_lookup:
        params["batters_lookup[]"] = batters_lookup

    return fetch_csv(STATCAST_SEARCH_URL, params, source="Statcast search")


def statcast_pitcher_search(
    pitchers_lookup: str | list[str],
    season: SeasonInput = DEFAULT_SEASON,
    game_type: str | GameType | list[str | GameType] = GameType.REGULAR_SEASON,
    start_dt: str = "",
    end_dt: str = "",
    month: str | Month | list[str | Month] = "",
    opponent: str | MlbTeam | list[str | MlbTeam] = "",
    debug: bool = False,
) -> pd.DataFrame:
    """
    Search for Statcast pitch-level data for pitcher(s) with custom filters.

    Args:
        pitchers_lookup (str | list[str]): The pitcher(s) to search for. (Required)
        season (int | str | list[int | str]): The season(s) to search for. Defaults to the current season.
        game_type (str | GameType | list[str | GameType]): The game type(s) to search for.
        start_dt (str): The start date in 'YYYY-MM-DD' format.
        end_dt (str): The end date in 'YYYY-MM-DD' format.
        month (str | Month | list[str | Month]): The month(s) to search for.
        opponent (str | MlbTeam | list[str | MlbTeam]): The opponent(s) to search for.

    Returns:
        pd.DataFrame: A DataFrame containing the Statcast pitch-level data for target pitcher(s).
    """

    if not pitchers_lookup:
        raise ValueError("pitchers_lookup is required")

    params = {
        "pitchers_lookup": pitchers_lookup,
        "season": season,
        "player_type": "pitcher",
        "game_type": game_type,
        "start_dt": start_dt,
        "end_dt": end_dt,
        "month": month,
        "opponent": opponent,
        "debug": debug,
    }

    return statcast_search(**params)


def statcast_batter_search(
    batters_lookup: str | list[str],
    season: SeasonInput = DEFAULT_SEASON,
    game_type: str | GameType | list[str | GameType] = GameType.REGULAR_SEASON,
    start_dt: str = "",
    end_dt: str = "",
    month: str | Month | list[str | Month] = "",
    opponent: str | MlbTeam | list[str | MlbTeam] = "",
    debug: bool = False,
) -> pd.DataFrame:
    """
    Search for Statcast pitch-level data for batter(s) with custom filters.

    Args:
        batters_lookup (str | list[str]): The batter(s) to search for. (Required)
        season (int | str | list[int | str]): The season(s) to search for. Defaults to the current season.
        game_type (str | GameType | list[str | GameType]): The game type(s) to search for.
        start_dt (str): The start date in 'YYYY-MM-DD' format.
        end_dt (str): The end date in 'YYYY-MM-DD' format.
        month (str | Month | list[str | Month]): The month(s) to search for.
        opponent (str | MlbTeam | list[str | MlbTeam]): The opponent(s) to search for.

    Returns:
        pd.DataFrame: A DataFrame containing the Statcast pitch-level data for target batter(s).
    """

    if not batters_lookup:
        raise ValueError("batters_lookup is required")

    params = {
        "batters_lookup": batters_lookup,
        "season": season,
        "player_type": "batter",
        "game_type": game_type,
        "start_dt": start_dt,
        "end_dt": end_dt,
        "month": month,
        "opponent": opponent,
        "debug": debug,
    }

    return statcast_search(**params)
