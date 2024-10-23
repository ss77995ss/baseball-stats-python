import pytest

from baseball_stats_python.statcast.statcast_search import (
    statcast_batter_search,
    statcast_pitcher_search,
)


def test_statcast_pitcher_search_invalid():
    with pytest.raises(ValueError) as e:
        statcast_pitcher_search(pitchers_lookup='')
    assert str(e.value) == 'pitchers_lookup is required'


def test_statcast_batter_search_invalid():
    with pytest.raises(ValueError) as e:
        statcast_batter_search(batters_lookup='')
    assert str(e.value) == 'batters_lookup is required'
