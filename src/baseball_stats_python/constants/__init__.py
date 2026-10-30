from datetime import date


def get_default_season(today: date) -> int:
    # Savant keeps last season as default through spring training.
    return today.year if today.month >= 4 else today.year - 1


# Latest queryable season, includes spring training before the default switches.
LATEST_SEASON = date.today().year
DEFAULT_SEASON = get_default_season(date.today())
