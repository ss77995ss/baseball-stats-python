# Statcast Runner Extra Bases Taken

## `runner_extra_bases_taken`

Function to get extra base taken data from each advanced opportunity for a specific runner. Based on Baseball Savant's [Runner Extra Bases Taken](https://baseballsavant.mlb.com/leaderboard/baserunning).

**Examples**

```python
from baseball_stats_python import runner_extra_bases_taken

# Get Corbin Carroll's runner extra bases taken data
runner_extra_bases_taken('682998')

# Get Corbin Carroll's runner extra bases taken data in 2023
runner_extra_bases_taken('682998', season='2023')

# Get Corbin Carroll's runner extra bases taken data in playoffs
runner_extra_bases_taken('682998', game_type=GameType.PLAYOFFS)
```

**Arguments**

| Argument             | Data Type           | Description                                                                                                                                                   |
| -------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| runner_id (Required) | `str`               | The MLBAM ID of the runner.                                                                                                                                   |
| game_type            | `str` or `GameType` | The game type to filter by. Can be `R` for regular season, `PO` for playoffs, or `All` for all games. Check enum [GameType](../enums/statcast_leaderboard.py) |
| season               | `str`               | The season to filter by. The earliest season available is 2016.                                                                                               |

**Return**

A DataFrame with columns that related to the [Runner Extra Bases Taken](https://baseballsavant.mlb.com/leaderboard/baserunning) leaderboard. The DataFrame will represent each advanced opportunity for a specific runner which contains data like `fielder_runs`, `runner_runs`, `base_out_text`, etc.
