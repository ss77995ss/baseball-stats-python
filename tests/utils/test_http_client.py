import http.server
import threading
import time

import pytest
import requests
from urllib3.response import HTTPResponse

from baseball_stats_python.utils import http_client


class _SlowHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(2)
        self.send_response(200)
        self.end_headers()

    def log_message(self, *args):
        pass


@pytest.fixture
def slow_server():
    server = http.server.HTTPServer(('127.0.0.1', 0), _SlowHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f'http://127.0.0.1:{server.server_port}'
    server.shutdown()


@pytest.fixture(autouse=True)
def restore_timeouts():
    saved = http_client.get_request_timeout()
    yield
    http_client.set_request_timeout(**saved)


def test_slow_server_raises_read_timeout(slow_server):
    http_client.set_request_timeout(read=0.5)
    start = time.monotonic()
    with pytest.raises(requests.exceptions.ReadTimeout):
        http_client.http_get(slow_server)
    assert time.monotonic() - start < 1.5


def test_search_uses_search_read_timeout(slow_server):
    http_client.set_request_timeout(read=5, search_read=0.5)
    with pytest.raises(requests.exceptions.ReadTimeout):
        http_client.http_get(slow_server, search=True)


def test_set_request_timeout_rejects_non_positive():
    with pytest.raises(ValueError):
        http_client.set_request_timeout(read=0)


def test_retry_after_is_capped():
    retry = http_client.session.get_adapter('https://').max_retries
    huge = HTTPResponse(headers={'Retry-After': '9999'}, status=503)
    small = HTTPResponse(headers={'Retry-After': '5'}, status=503)
    assert retry.get_retry_after(huge) == http_client.MAX_RETRY_AFTER
    assert retry.get_retry_after(small) == 5
