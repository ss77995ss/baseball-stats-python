"""Season validation shared by every data source."""

from ..constants import DEFAULT_SEASON

SeasonInput = int | str | list[int | str]


def seasons_between(first: int, last: int = DEFAULT_SEASON) -> list[str]:
    """Seasons from first to last (inclusive), as strings."""
    return [str(year) for year in range(first, last + 1)]


def build_season_param(
    season: SeasonInput,
    available: list[str],
    *,
    aliases: dict[str, list[str]] | None = None,
    default: str = str(DEFAULT_SEASON),
) -> str:
    """
    Validate season input and build the pipe-separated value sources expect.

    Accepts an int or str season ('2025' or 2025), a list of them, '' for
    the default season, or an alias such as 'all'.
    """
    if isinstance(season, bool) or not isinstance(season, int | str | list):
        raise ValueError(f'Invalid type for season: {type(season)}')

    if isinstance(season, list):
        values = [str(s) for s in season]
        if any(value not in available for value in values):
            raise ValueError(f'Invalid seasons: {season}')
        return '|'.join(values)

    value = str(season)
    if value == '':
        return default
    if aliases and value in aliases:
        return '|'.join(aliases[value])
    if value not in available:
        raise ValueError(f'Invalid season: {season}')
    return value
