import requests
import io
import pandas as pd

from ..utils.statcast import get_season_param_str, get_game_type_param_str, get_month_param_str, get_team_param_str
from ..enums.statcast import MlbTeam, GameType, Month

STATCAST_SEARCH_URL = "https://baseballsavant.mlb.com/statcast_search/csv"


def statcast_search(season: str | list[str] = "2024", player_type: str = "pitcher",
                    game_type: str | GameType | list[str |
                                                     GameType] = GameType.REGULAR_SEASON,
                    start_dt: str = "", end_dt: str = "", month: str | Month | list[str | Month] = "",
                    pitchers_lookup: str | list[str] = "", batters_lookup: str | list[str] = "",
                    team: str | MlbTeam | list[str | MlbTeam] = "", opponent: str | MlbTeam | list[str | MlbTeam] = "") -> pd.DataFrame:
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
        "type": "details"
    }

    if pitchers_lookup:
        params["pitchers_lookup[]"] = pitchers_lookup

    if batters_lookup:
        params["batters_lookup[]"] = batters_lookup

    response = requests.get(STATCAST_SEARCH_URL, params=params)

    print(response.url)

    if response.status_code == 200:
        csv_content = io.StringIO(response.text)

        return pd.read_csv(csv_content)
    else:
        raise Exception(
            f"Failed to fetch data: {response.status_code} - {response.text}")
