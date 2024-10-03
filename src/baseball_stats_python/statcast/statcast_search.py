import requests
import io
import pandas as pd


STATCAST_SEARCH_URL = "https://baseballsavant.mlb.com/statcast_search/csv"


def statcast_search(season: str | list[str] = "2024", player_type: str = "pitcher", game_type: str | list[str] = "R|",
                    start_dt: str = "", end_dt: str = "", month: str | list[str] = "",
                    pitchers_lookup: str | list[str] = "", batters_lookup: str | list[str] = "",
                    team: str | list[str] = "", opponent: str | list[str] = "") -> pd.DataFrame:
    """
    Search for Statcast pitch-level data with custom filters.

    Args:
        season (str | list[str]): The season(s) to search for.
        player_type (str): The type of player to search for.
        game_type (str | list[str]): The game type(s) to search for.
        start_dt (str): The start date in 'YYYY-MM-DD' format.
        end_dt (str): The end date in 'YYYY-MM-DD' format.
        month (str | list[str]): The month(s) to search for.
        pitchers_lookup (str | list[str]): The pitcher(s) to search for.
        batters_lookup (str | list[str]): The batter(s) to search for.
        team (str | list[str]): The team(s) to search for.
        opponent (str | list[str]): The opponent(s) to search for.

    Returns:
        pd.DataFrame: A DataFrame containing the Statcast pitch-level data.
    """

    params = {
        "all": "true",
        "player_type": player_type,
        "hfSea": season if type(season) == str else "|".join(season),
        "hfGT": game_type if type(game_type) == str else "|".join(game_type),
        "game_date_gt": start_dt,
        "game_date_lt": end_dt,
        "hfMo": month if type(month) == str else "|".join(month),
        "hfTeam": team if type(team) == str else "|".join(team),
        "hfOpponent": opponent if type(opponent) == str else "|".join(opponent),
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
