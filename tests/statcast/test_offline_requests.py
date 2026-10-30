import logging

import pytest

from baseball_stats_python import mlbam_id_search, statcast_search
from baseball_stats_python.constants import DEFAULT_SEASON
from baseball_stats_python.errors import RequestError


def test_statcast_search_parses_csv_and_defaults_to_current_season(fake_get):
    fake_get.respond_text('pitch_type,release_speed\nFF,97.1\n')

    df = statcast_search(pitchers_lookup='477132')

    assert df['pitch_type'].iloc[0] == 'FF'
    assert fake_get.calls[0]['params']['hfSea'] == str(DEFAULT_SEASON)


def test_statcast_search_raises_request_error(fake_get):
    fake_get.respond_text('boom', status_code=500)

    with pytest.raises(RequestError):
        statcast_search()


def test_mlbam_id_search_limit(fake_get):
    fake_get.respond_json([{'id': i} for i in range(15)])

    assert len(mlbam_id_search('smith')) == 10
    assert len(mlbam_id_search('smith', limit=3)) == 3
    assert len(mlbam_id_search('smith', limit=None)) == 15


def test_library_is_quiet_and_leaves_root_logger_alone(fake_get, capsys):
    root = logging.getLogger()
    level, handlers = root.level, list(root.handlers)
    fake_get.respond_text('a\n1\n')

    statcast_search(debug=True)

    assert capsys.readouterr().out == ''
    assert root.level == level
    assert root.handlers == handlers
