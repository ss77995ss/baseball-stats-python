from datetime import date

import pytest

from baseball_stats_python.constants import DEFAULT_SEASON, current_season
from baseball_stats_python.utils.minor import get_minor_season_param_str
from baseball_stats_python.utils.statcast import get_season_param_str
from baseball_stats_python.utils.wbc import get_wbc_season_param_str


def test_current_season_rolls_over_in_march():
    assert current_season(date(2026, 2, 28)) == 2025
    assert current_season(date(2026, 3, 1)) == 2026


def test_current_season_is_always_accepted():
    assert get_season_param_str(str(DEFAULT_SEASON)) == str(DEFAULT_SEASON)
    assert get_minor_season_param_str(DEFAULT_SEASON) == str(DEFAULT_SEASON)


def test_int_seasons_are_accepted():
    assert get_season_param_str(2024) == '2024'
    assert get_season_param_str([2024, '2023']) == '2024|2023'


def test_bool_is_not_a_season():
    with pytest.raises(ValueError):
        get_season_param_str(True)


def test_wbc_defaults_to_latest_edition():
    assert get_wbc_season_param_str('') == '2026'
    with pytest.raises(ValueError):
        get_wbc_season_param_str('2025')
