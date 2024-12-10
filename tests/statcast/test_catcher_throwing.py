import pytest

from baseball_stats_python.statcast.catcher_throwing import catcher_throwing


def test_catcher_throwing_invalid():
    with pytest.raises(ValueError) as e:
        catcher_throwing('')
    assert str(e.value) == 'catcher_id is required'

    with pytest.raises(ValueError) as e:
        catcher_throwing('669257', 'invalid')
    assert str(e.value) == 'Invalid game type: invalid'

    with pytest.raises(ValueError) as e:
        catcher_throwing('669257', 123)
    assert str(e.value) == f'Invalid type for game_type: {int}'

    with pytest.raises(ValueError) as e:
        catcher_throwing('669257', season='2015')
    assert str(e.value) == 'Invalid season: 2015, The earliest season available is 2016'

    with pytest.raises(ValueError) as e:
        catcher_throwing('669257', game_type='RRR')
    assert str(e.value) == 'Invalid game type: RRR'
