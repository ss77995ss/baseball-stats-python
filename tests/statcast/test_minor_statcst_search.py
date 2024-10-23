import pytest

from baseball_stats_python.statcast.minor_statcast_search import (
    minor_statcast_batter_search,
    minor_statcast_pitcher_search,
)


def test_minor_statcast_pitcher_search_invalid():
    with pytest.raises(ValueError) as e:
        minor_statcast_pitcher_search(pitchers_lookup='')
    assert str(e.value) == 'pitchers_lookup is required'


def test_minor_statcast_batter_search_invalid():
    with pytest.raises(ValueError) as e:
        minor_statcast_batter_search(batters_lookup='')
    assert str(e.value) == 'batters_lookup is required'
