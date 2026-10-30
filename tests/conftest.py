import json

import pytest

from baseball_stats_python.utils import http_client


class FakeResponse:
    def __init__(self, status_code=200, text='', url='https://fake.test'):
        self.status_code = status_code
        self.text = text
        self.url = url

    def json(self):
        return json.loads(self.text)


class FakeGet:
    """Stands in for the shared session's get(); records every call."""

    def __init__(self):
        self.calls = []
        self.response = FakeResponse()
        self.exc = None

    def __call__(self, url, params=None, **kwargs):
        self.calls.append({'url': url, 'params': params, **kwargs})
        if self.exc is not None:
            raise self.exc
        return self.response

    def respond_json(self, data, status_code=200):
        self.response = FakeResponse(status_code, json.dumps(data))

    def respond_text(self, text, status_code=200):
        self.response = FakeResponse(status_code, text)


@pytest.fixture
def fake_get(monkeypatch):
    """Replace every outgoing request with a canned response, offline."""
    fake = FakeGet()
    monkeypatch.setattr(http_client.session, 'get', fake)
    return fake
