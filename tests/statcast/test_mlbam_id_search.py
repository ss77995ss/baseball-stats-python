import pytest

from baseball_stats_python.statcast.mlbam_id_search import mlbam_id_search


def test_mlbam_id_search_invalid():
    with pytest.raises(ValueError) as e:
        mlbam_id_search('')
    assert str(e.value) == 'player_name is required'
