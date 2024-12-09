# Statcast Catcher Throwing

## `catcher_throwing`

Function to get catcher throwing data from each stolen base attempt for a specific catcher. Based on Baseball Savant's [Catcher Throwing](https://baseballsavant.mlb.com/leaderboard/catcher-throwing).

**Examples**

```python
from baseball_stats_python import catcher_throwing

# Get Will Smith's catcher throwing data
catcher_throwing('669257')

# Get Will Smith's catcher throwing data in 2023
catcher_throwing('669257', season='2023')

# Get Will Smith's catcher throwing data in playoffs
catcher_throwing('669257', game_type=GameType.PLAYOFFS)
```

**Arguments**

| Argument              | Data Type           | Description                                                                                                                                                   |
| --------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| catcher_id (Required) | `str`               | The MLBAM ID of the catcher.                                                                                                                                  |
| game_type             | `str` or `GameType` | The game type to filter by. Can be `R` for regular season, `PO` for playoffs, or `All` for all games. Check enum [GameType](../enums/statcast_leaderboard.py) |
| season                | `str`               | The season to filter by. The earliest season available is 2016.                                                                                               |

**Return**

A DataFrame with columns that related to the [Catcher Throwing](https://baseballsavant.mlb.com/leaderboard/catcher-throwing) leaderboard. The DataFrame will represent each stolen base attempt for a specific catcher which contains data like `pop_time`, `throw_type`, `r_primary_lead`, etc.
