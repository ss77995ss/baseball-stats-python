from datetime import datetime

import pytest

from baseball_stats_python.utils.utils import validate_date_format, validate_date_range


def test_validate_date_format():
    with pytest.raises(ValueError) as e:
        validate_date_format('2024/07/01')
    assert "does not match format '%Y-%m-%d'" in str(e.value)

    date = validate_date_format('2024-07-01')
    assert isinstance(date, datetime)
    assert date == datetime(2024, 7, 1)


def test_validate_date_range():
    with pytest.raises(ValueError) as e:
        validate_date_range('2024-07-02', '2024-07-01')
    assert str(e.value) == 'end_dt cannot be earlier than start_dt.'

    with pytest.raises(ValueError) as e:
        validate_date_range('2024/07/01', '2024/07/02')

    assert "does not match format '%Y-%m-%d'" in str(e.value)

    validate_date_range('2024-07-01', '2024-07-02')
    validate_date_range('2024-07-01', '')
    validate_date_range('', '2024-07-02')
    validate_date_range('', '')
