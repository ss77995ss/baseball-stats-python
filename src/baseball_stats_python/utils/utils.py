from datetime import datetime


def validate_date_format(dt: str) -> datetime:
    date_format = '%Y-%m-%d'
    try:
        date = datetime.strptime(dt, date_format)
        return date
    except ValueError as e:
        raise ValueError(e)


def validate_date_range(start_dt: str, end_dt: str) -> None:
    if start_dt:
        start_date = validate_date_format(start_dt)
    if end_dt:
        end_date = validate_date_format(end_dt)

    if start_dt and end_dt and end_date < start_date:
        raise ValueError('end_dt cannot be earlier than start_dt.')
