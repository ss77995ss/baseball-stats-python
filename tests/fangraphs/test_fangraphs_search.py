import json

import pandas as pd
import pytest
import requests

from baseball_stats_python.fangraphs.fangraphs_search import fg_batting, fg_pitching


def make_fake_get(captured, data):
    def fake_get(url, params=None):
        captured["params"] = params

        class FakeResponse:
            content = json.dumps({"data": data}).encode()
            url = "https://fake"

            def raise_for_status(self):
                pass

        return FakeResponse()

    return fake_get


def test_fg_batting_cleans_html_and_sends_bat_stats(monkeypatch):
    captured = {}
    monkeypatch.setattr(
        requests,
        "get",
        make_fake_get(captured, [{"Name": '<a href="x">Mike Trout</a>', "Team": "<a>LAA</a>"}]),
    )

    df = fg_batting()

    assert isinstance(df, pd.DataFrame)
    assert df["Name"].iloc[0] == "Mike Trout"
    assert df["Team"].iloc[0] == "LAA"
    assert captured["params"]["stats"] == "bat"


def test_fg_pitching_sends_pit_stats(monkeypatch):
    captured = {}
    monkeypatch.setattr(
        requests,
        "get",
        make_fake_get(captured, [{"Name": '<a href="x">Gerrit Cole</a>', "Team": "<a>NYY</a>"}]),
    )

    df = fg_pitching()

    assert df["Name"].iloc[0] == "Gerrit Cole"
    assert captured["params"]["stats"] == "pit"


def test_fg_search_returns_empty_dataframe(monkeypatch):
    captured = {}
    monkeypatch.setattr(requests, "get", make_fake_get(captured, []))

    df = fg_batting()

    assert isinstance(df, pd.DataFrame)
    assert df.empty


def test_fg_search_wraps_request_exception(monkeypatch):
    def boom(url, params=None):
        raise requests.exceptions.RequestException("network down")

    monkeypatch.setattr(requests, "get", boom)

    with pytest.raises(Exception) as e:
        fg_batting()
    assert str(e.value).startswith("Failed to fetch data:")
