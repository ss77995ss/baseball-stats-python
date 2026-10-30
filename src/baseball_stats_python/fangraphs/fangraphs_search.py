import logging

import pandas as pd

from ..constants import DEFAULT_SEASON
from ..utils.fetch import fetch_json
from ..utils.log import enable_debug_logging
from ..utils.utils import extract_text_from_html

FANGRAPHS_MAIN_URL = "https://www.fangraphs.com/api/leaders/major-league/data"

logger = logging.getLogger(__name__)


def fangraphs_search(
    stats: str = "bat",
    age: int = 0,
    pos: str = "all",
    lg: str = "all",
    qual: int | str = "y",
    season: int = DEFAULT_SEASON,
    season1: int | None = None,
    start_date: str = "",
    end_date: str = "",
    month: int = 0,
    hand: str = "",
    team: str = "",
    pageitems: int = 10000,
    pagenum: int = 1,
    ind: int = 0,
    rost: int = 0,
    players: str = "",
    type: int = 8,
    postseason: str = "",
    heatmapqual: str = "",
    sortdir: str = "default",
    sortstat: str = "WAR",
    debug: bool = False,
) -> pd.DataFrame:
    """
    Get leaderboard data from the Fangraphs major-league leaders API.

    Mirrors the query parameters of the Fangraphs leaderboard page
    (https://www.fangraphs.com/leaders/major-league). All filters are optional;
    the defaults return the current-season qualified leaderboard.
    Not all arguments' descriptions are accurate. Still need to be updated.

    Args:
        stats (str): Stat group to fetch — "bat" for batting or "pit" for pitching.
        age (int): Filter by player age. 0 means no age filter.
        pos (str): Position filter (e.g. "all", "c", "1b", "of", "np" for non-pitchers).
        lg (str): League filter — "all", "al", or "nl".
        qual (int | str): Plate-appearance/innings qualifier. "y" for the qualified
            threshold, or an integer for a custom minimum; 0 means no minimum.
        season (int): End season of the range to query. Defaults to the current season.
        season1 (int | None): Start season of the range. Defaults to `season` (a single season).
        start_date (str): Range start date in "YYYY-MM-DD" format (should set month to 1000 to activate this filter).
            Defaults to March 1 of `season1`.
        end_date (str): Range end date in "YYYY-MM-DD" format (should set month to 1000 to activate this filter).
            Defaults to November 1 of `season`.
        month (int): Split by calendar month/period. 0 means full season. 1000 means use start_date and end_date to filter by date.
        hand (str): Batter/pitcher handedness filter — "R", "L", or "" for both.
        team (str): Team filter by Fangraphs team id; "" means all teams.
        pageitems (int): Number of rows per page. default set to 10000 to get all possible rows.
        pagenum (int): Page number to fetch.
        ind (int): Split seasons individually (1) or aggregate the range into one row (0).
        rost (int): Roster filter — 0 for all players, 1 for active roster only.
        players (str): Filter to specific player id(s); "" means all players.
        type (int): Stat dashboard/column set id (8 is the default dashboard).
        postseason (str): Set to a truthy value to query postseason stats; "" for regular season.
        heatmapqual (str): Heatmap qualifier flag passed through to the API.
        sortdir (str): Sort direction — "default", "asc", or "desc".
        sortstat (str): Column to sort by (e.g. "WAR").
        debug (bool): If True, raise the logger to DEBUG level to print the request params and URL.

    Returns:
        pd.DataFrame: The leaderboard rows, with HTML stripped from the Name and Team
        columns. An empty DataFrame is returned when the API has no matching data.
    """
    if debug:
        enable_debug_logging()

    if season1 is None:
        season1 = season
    start_date = start_date or f"{season1}-03-01"
    end_date = end_date or f"{season}-11-01"

    params = {
        "age": age,
        "pos": pos,
        "stats": stats,
        "lg": lg,
        "qual": qual,
        "season": season,
        "season1": season1,
        "startdate": start_date,
        "enddate": end_date,
        "month": month,
        "hand": hand,
        "team": team,
        "pageitems": pageitems,
        "pagenum": pagenum,
        "ind": ind,
        "rost": rost,
        "players": players,
        "type": type,
        "postseason": postseason,
        "heatmapqual": heatmapqual,
        "sortdir": sortdir,
        "sortstat": sortstat,
    }

    data = fetch_json(FANGRAPHS_MAIN_URL, params, source="FanGraphs leaderboard")
    df = pd.DataFrame(data["data"])

    if df.empty:
        logger.warning("No data found")
        return df

    df["Name"] = df["Name"].apply(extract_text_from_html)
    df["Team"] = df["Team"].apply(extract_text_from_html)

    return df


def fg_batting(
    qual: int | str = 0, season: int = DEFAULT_SEASON, debug: bool = False
) -> pd.DataFrame:
    """
    Get the batting leaderboard from Fangraphs.

    Convenience wrapper around `fangraphs_search` with stats="bat".
    Currently only supports single season queries. Use `fangraphs_search` for multiple season queries.

    Args:
        qual (int | str): Plate-appearance qualifier — "y" for the qualified
            threshold, an integer for a custom minimum, or 0 for no minimum.
        season (int): Season to query.
        debug (bool): If True, log the request params and URL at DEBUG level.

    Returns:
        pd.DataFrame: The batting leaderboard, with HTML stripped from Name and Team.
    """
    return fangraphs_search(
        stats="bat", qual=qual, season=season, season1=season, debug=debug
    )


def fg_pitching(
    qual: int | str = 0, season: int = DEFAULT_SEASON, debug: bool = False
) -> pd.DataFrame:
    """
    Get the pitching leaderboard from Fangraphs.

    Convenience wrapper around `fangraphs_search` with stats="pit".
    Currently only supports single season queries. Use `fangraphs_search` for multiple season queries.

    Args:
        qual (int | str): Innings-pitched qualifier — "y" for the qualified
            threshold, an integer for a custom minimum, or 0 for no minimum.
        season (int): Season to query.
        debug (bool): If True, log the request params and URL at DEBUG level.

    Returns:
        pd.DataFrame: The pitching leaderboard, with HTML stripped from Name and Team.
    """
    return fangraphs_search(
        stats="pit", qual=qual, season=season, season1=season, debug=debug
    )
