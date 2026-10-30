from datetime import date

# Regular-season data starts showing up in March (spring training);
# before that, "the current season" still means last year's.
SEASON_START_MONTH = 3


def current_season(today: date | None = None) -> int:
    """Return the most recent season that has started."""
    today = today or date.today()
    return today.year if today.month >= SEASON_START_MONTH else today.year - 1


DEFAULT_SEASON = current_season()
