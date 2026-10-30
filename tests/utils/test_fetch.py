import pytest
import requests

from baseball_stats_python.errors import (
    BaseballStatsError,
    RequestError,
    RequestTimeoutError,
)
from baseball_stats_python.utils.fetch import fetch_csv, fetch_json
from baseball_stats_python.utils.http_client import get_request_timeout


def test_fetch_json_returns_decoded_body(fake_get):
    fake_get.respond_json({'ok': True})
    assert fetch_json('https://x.test', source='test') == {'ok': True}


def test_error_status_raises_request_error_with_details(fake_get):
    fake_get.respond_text('x' * 1000, status_code=500)

    with pytest.raises(RequestError) as e:
        fetch_json('https://x.test', source='test')

    assert e.value.status_code == 500
    assert len(str(e.value)) < 300  # long bodies are shortened
    assert isinstance(e.value, BaseballStatsError)


def test_gateway_timeout_on_search_suggests_narrower_query(fake_get):
    fake_get.respond_text('', status_code=504)

    with pytest.raises(RequestTimeoutError) as e:
        fetch_csv('https://x.test', source='test')

    assert 'narrower' in str(e.value)


def test_client_timeout_becomes_request_timeout_error(fake_get):
    fake_get.exc = requests.exceptions.ReadTimeout('slow')

    with pytest.raises(RequestTimeoutError):
        fetch_csv('https://x.test', source='test')


def test_connection_error_is_request_error_not_timeout(fake_get):
    fake_get.exc = requests.exceptions.ConnectionError('down')

    with pytest.raises(RequestError) as e:
        fetch_json('https://x.test', source='test')

    assert not isinstance(e.value, RequestTimeoutError)


def test_invalid_json_raises_request_error(fake_get):
    fake_get.respond_text('<html>oops</html>')

    with pytest.raises(RequestError):
        fetch_json('https://x.test', source='test')


def test_csv_search_uses_search_timeout(fake_get):
    fake_get.respond_text('a,b\n1,2\n')

    df = fetch_csv('https://x.test', source='test')

    assert df.to_dict('records') == [{'a': 1, 'b': 2}]
    assert fake_get.calls[0]['timeout'][1] == get_request_timeout()['search_read']
