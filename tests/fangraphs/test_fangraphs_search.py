import pandas as pd
import pytest
import requests

from baseball_stats_python.errors import RequestError
from baseball_stats_python.fangraphs.fangraphs_search import (
    fangraphs_search,
    fg_batting,
    fg_pitching,
)


def test_fg_batting_cleans_html_and_sends_bat_stats(fake_get):
    fake_get.respond_json(
        {'data': [{'Name': '<a href="x">Mike Trout</a>', 'Team': '<a>LAA</a>'}]}
    )

    df = fg_batting()

    assert isinstance(df, pd.DataFrame)
    assert df['Name'].iloc[0] == 'Mike Trout'
    assert df['Team'].iloc[0] == 'LAA'
    assert fake_get.calls[0]['params']['stats'] == 'bat'


def test_fg_pitching_sends_pit_stats(fake_get):
    fake_get.respond_json(
        {'data': [{'Name': '<a href="x">Gerrit Cole</a>', 'Team': '<a>NYY</a>'}]}
    )

    df = fg_pitching()

    assert df['Name'].iloc[0] == 'Gerrit Cole'
    assert fake_get.calls[0]['params']['stats'] == 'pit'


def test_fg_search_returns_empty_dataframe(fake_get):
    fake_get.respond_json({'data': []})

    df = fg_batting()

    assert isinstance(df, pd.DataFrame)
    assert df.empty


def test_fg_search_dates_follow_season(fake_get):
    fake_get.respond_json({'data': []})

    fangraphs_search(season=2024)

    params = fake_get.calls[0]['params']
    assert params['season1'] == 2024
    assert params['startdate'] == '2024-03-01'
    assert params['enddate'] == '2024-11-01'


def test_fg_search_wraps_request_exception(fake_get):
    fake_get.exc = requests.exceptions.RequestException('network down')

    with pytest.raises(RequestError) as e:
        fg_batting()
    assert str(e.value).startswith('Failed to fetch data:')
