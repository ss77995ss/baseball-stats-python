from datetime import datetime

import pytest

from baseball_stats_python.enums.statcast import GameType, MlbTeam, Month
from baseball_stats_python.utils.statcast import (
    CURRENT_SEASON,
    get_game_type_param_str,
    get_month_param_str,
    get_season_param_str,
    get_team_param_str,
)


def test_get_season_param_str():
    assert get_season_param_str("2024") == "2024"
    assert get_season_param_str(["2024", "2023"]) == "2024|2023"
    assert get_season_param_str("") == str(CURRENT_SEASON)


def test_get_season_param_str_invalid():
    with pytest.raises(ValueError) as e:
        get_season_param_str("2024.5")
    assert str(e.value) == "Invalid season: 2024.5"

    with pytest.raises(ValueError) as e:
        get_season_param_str("2007")
    assert str(e.value) == "Invalid season: 2007"

    with pytest.raises(ValueError) as e:
        current_year_plus_one = datetime.now().year + 1
        get_season_param_str(str(current_year_plus_one))
    assert str(e.value) == f"Invalid season: {current_year_plus_one}"

    with pytest.raises(ValueError) as e:
        test_season = ["2024.5", "2023"]
        get_season_param_str(test_season)
    assert str(e.value) == f"Invalid seasons: {test_season}"

    with pytest.raises(ValueError) as e:
        get_season_param_str(2025)
    assert str(e.value) == f"Invalid type for season: {int}"

    with pytest.raises(ValueError) as e:
        test_season = ["2024", 2023]
        get_season_param_str(test_season)
    assert str(e.value) == f"Invalid seasons: {test_season}"


def test_get_game_type_param_str():
    assert get_game_type_param_str("R") == "R|"
    assert get_game_type_param_str(["R", "PO"]) == "R|PO|"
    assert get_game_type_param_str(["R", "PO", "A"]) == "R|PO|A|"
    assert get_game_type_param_str(GameType.REGULAR_SEASON) == "R|"
    assert (
        get_game_type_param_str([GameType.REGULAR_SEASON, GameType.PLAYOFFS]) == "R|PO|"
    )
    assert (
        get_game_type_param_str(["R", GameType.PLAYOFFS, GameType.ALL_STAR])
        == "R|PO|A|"
    )
    assert get_game_type_param_str("") == "R|"
    assert get_game_type_param_str("all") == "R|PO|F|D|L|W|S|A|"


def test_get_game_type_param_str_invalid():
    with pytest.raises(ValueError) as e:
        get_game_type_param_str("regular_season")
    assert str(e.value) == "Invalid game type: regular_season"

    with pytest.raises(ValueError) as e:
        get_game_type_param_str([GameType.REGULAR_SEASON, "playoffs"])
    assert str(e.value) == "Invalid game types: R|playoffs"

    with pytest.raises(ValueError) as e:
        get_game_type_param_str(Month.AUGUST)
    assert str(e.value) == f"Invalid type for game_type: {type(Month.AUGUST)}"


def test_get_month_param_str():
    assert get_month_param_str("8") == "8|"
    assert get_month_param_str(["8", "9"]) == "8|9|"
    assert get_month_param_str(Month.AUGUST) == "8|"
    assert get_month_param_str([Month.AUGUST, Month.SEPTEMBER_AND_OCTOBER]) == "8|9|"
    assert get_month_param_str("") == ""
    assert get_month_param_str("all") == "4|5|6|7|8|9|"


def test_get_month_param_str_invalid():
    with pytest.raises(ValueError) as e:
        get_month_param_str("3")
    assert str(e.value) == "Invalid month: 3"

    with pytest.raises(ValueError) as e:
        get_month_param_str(["3", "4"])
    assert str(e.value) == "Invalid months: 3|4"

    with pytest.raises(ValueError) as e:
        get_month_param_str(2024)
    assert str(e.value) == f"Invalid type for month: {int}"


def test_get_team_param_str():
    assert get_team_param_str("SD") == "SD|"
    assert get_team_param_str(["SD", "SF"]) == "SD|SF|"
    assert get_team_param_str(MlbTeam.PADRES) == "SD|"
    assert get_team_param_str([MlbTeam.PADRES, MlbTeam.GIANTS]) == "SD|SF|"
    assert get_team_param_str("") == ""


def test_get_team_param_str_invalid():
    with pytest.raises(ValueError) as e:
        get_team_param_str("ARI")
    assert str(e.value) == "Invalid team: ARI"

    with pytest.raises(ValueError) as e:
        get_team_param_str(["SD", "SF", "LA"])
    assert str(e.value) == "Invalid teams: SD|SF|LA"

    with pytest.raises(ValueError) as e:
        get_team_param_str(Month.JUNE)
    assert str(e.value) == f"Invalid type for team: {type(Month.JUNE)}"
