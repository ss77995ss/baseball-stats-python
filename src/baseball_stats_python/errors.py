"""Errors raised by baseball_stats_python.

Every error the package raises on purpose inherits from BaseballStatsError,
so callers can catch them all with one except clause. Invalid arguments
still raise ValueError, as before.
"""


class BaseballStatsError(Exception):
    """Base class for every error raised by this package."""


class RequestError(BaseballStatsError):
    """A request to a data source failed or returned an error status."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        url: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.url = url


class RequestTimeoutError(RequestError):
    """The data source did not answer in time.

    For Statcast searches this usually means the query is too large;
    a narrower date range or fewer players will help.
    """
