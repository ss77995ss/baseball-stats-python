"""Fetch data from a source and turn failures into package errors.

Every data source goes through these helpers, so timeouts, retries,
logging and error messages behave the same everywhere.
"""

import io
import logging
from typing import Any

import pandas as pd
import requests

from ..errors import RequestError, RequestTimeoutError
from . import http_client

logger = logging.getLogger(__name__)

_MAX_BODY_IN_MESSAGE = 200
_SEARCH_HINT = ' Try a narrower date range or fewer players.'


def _short(text: str) -> str:
    text = ' '.join(text.split())
    if len(text) > _MAX_BODY_IN_MESSAGE:
        return text[:_MAX_BODY_IN_MESSAGE] + '…'
    return text


def fetch(
    url: str,
    params: dict[str, Any] | None = None,
    *,
    source: str,
    search: bool = False,
) -> requests.Response:
    """GET a URL and return the response, or raise a RequestError."""
    logger.info('Fetching %s', source)
    logger.debug('URL: %s params: %s', url, params)
    hint = _SEARCH_HINT if search else ''

    try:
        response = http_client.http_get(url, params=params, search=search)
    except requests.exceptions.Timeout as e:
        raise RequestTimeoutError(
            f'Failed to fetch data: {source} timed out.{hint}', url=url
        ) from e
    except requests.exceptions.RequestException as e:
        raise RequestError(f'Failed to fetch data: {e}', url=url) from e

    logger.debug('Response %s from %s', response.status_code, response.url)

    if response.status_code == 504:
        raise RequestTimeoutError(
            f'Failed to fetch data: {source} timed out on the server (504).{hint}',
            status_code=504,
            url=response.url,
        )
    if response.status_code != 200:
        raise RequestError(
            f'Failed to fetch data: {response.status_code} - {_short(response.text)}',
            status_code=response.status_code,
            url=response.url,
        )

    logger.info('Fetched %s', source)
    return response


def fetch_json(url: str, params: dict[str, Any] | None = None, *, source: str) -> Any:
    """GET a URL and decode its JSON body."""
    response = fetch(url, params, source=source)
    try:
        return response.json()
    except ValueError as e:
        raise RequestError(
            f'Failed to parse {source} response as JSON: {_short(response.text)}',
            status_code=response.status_code,
            url=response.url,
        ) from e


def fetch_csv(
    url: str, params: dict[str, Any] | None = None, *, source: str
) -> pd.DataFrame:
    """GET a CSV search result (with the longer search timeout) as a DataFrame."""
    response = fetch(url, params, source=source, search=True)
    return pd.read_csv(io.StringIO(response.text))
