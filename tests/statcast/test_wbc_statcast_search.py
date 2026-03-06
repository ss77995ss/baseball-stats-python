import pytest

from baseball_stats_python.statcast.wbc_statcast_search import (
    wbc_statcast_batter_search,
    wbc_statcast_pitcher_search,
)


def test_wbc_statcast_pitcher_search_invalid():
    with pytest.raises(ValueError) as e:
        wbc_statcast_pitcher_search(pitchers_lookup="")
    assert str(e.value) == "pitchers_lookup is required"


def test_wbc_statcast_batter_search_invalid():
    with pytest.raises(ValueError) as e:
        wbc_statcast_batter_search(batters_lookup="")
    assert str(e.value) == "batters_lookup is required"
