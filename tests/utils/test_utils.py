import pytest

from baseball_stats_python.utils.utils import validate_date_range

def test_validate_date_range():
    with pytest.raises(ValueError) as e:
        validate_date_range('2024-07-02', '2024-07-01')
    assert str(e.value) == "Invalid date format or range: end_dt cannot be earlier than start_dt."
    
    with pytest.raises(ValueError) as e:
        validate_date_range('2024/07/01', '2024/07/02')
        
    assert "Invalid date format or range" in str(e.value)
    assert "does not match format '%Y-%m-%d'" in str(e.value)