"""Shared HTTP session with timeouts and retries for every request."""

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Seconds to wait for the TCP/TLS connection to open.
CONNECT_TIMEOUT = 10.0

# Seconds to wait for data from light JSON endpoints
# (player search, catcher throwing, runner stats, FanGraphs).
READ_TIMEOUT = 30.0

# Seconds to wait for data from the Statcast CSV searches.
# Keep this slightly above Baseball Savant's own server-side limit for a
# single query: once Savant gives up it answers with a 5xx anyway, so
# waiting longer than that only hangs the caller.
# Placeholder until measured with measure_savant_timeout.py.
SEARCH_READ_TIMEOUT = 120.0

# Never sleep longer than this, whatever Retry-After the server sends.
MAX_RETRY_AFTER = 60.0

_timeouts = {
    'connect': CONNECT_TIMEOUT,
    'read': READ_TIMEOUT,
    'search_read': SEARCH_READ_TIMEOUT,
}


class _CappedRetry(Retry):
    """Honour the server's Retry-After header, but only up to a cap."""

    def get_retry_after(self, response):
        retry_after = super().get_retry_after(response)
        if retry_after is None:
            return None
        return min(retry_after, MAX_RETRY_AFTER)


def _build_session() -> requests.Session:
    retry = _CappedRetry(
        total=3,
        connect=3,
        # Re-raise read timeouts right away: retrying a query that was
        # too slow would just multiply the wait.
        read=False,
        status=3,
        backoff_factor=1,
        # 504 is left out on purpose: it usually means the query itself
        # is too large, and repeating it will not help.
        status_forcelist=(429, 500, 502, 503),
        allowed_methods=frozenset({'GET'}),
        respect_retry_after_header=True,
        raise_on_status=False,
    )
    session = requests.Session()
    session.mount('https://', HTTPAdapter(max_retries=retry))
    return session


session = _build_session()


def set_request_timeout(
    connect: float | None = None,
    read: float | None = None,
    search_read: float | None = None,
) -> None:
    """
    Change the timeouts (in seconds) used for every request.

    Args:
        connect (float | None): Time allowed to open a connection.
        read (float | None): Time allowed between bytes for light endpoints.
        search_read (float | None): Time allowed between bytes for Statcast CSV searches.
    """
    for key, value in (
        ('connect', connect),
        ('read', read),
        ('search_read', search_read),
    ):
        if value is None:
            continue
        if value <= 0:
            raise ValueError(f'{key} timeout must be greater than 0')
        _timeouts[key] = float(value)


def get_request_timeout() -> dict[str, float]:
    """Return the timeouts currently in use."""
    return dict(_timeouts)


def http_get(url: str, *, search: bool = False, **kwargs) -> requests.Response:
    """GET a URL with the package's timeouts and retry policy."""
    read = _timeouts['search_read'] if search else _timeouts['read']
    kwargs.setdefault('timeout', (_timeouts['connect'], read))
    return session.get(url, **kwargs)
