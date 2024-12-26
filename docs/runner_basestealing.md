# Statcast Runner Basestealing

## `runner_basestealing`

Function to get baserunner stealing base data from each stolen base attempt. Attempts include successful stolen bases (`SB`), advances via balk (`BK`), caught stealing (`CS`), and pickoffs (`PK`). Also pickoff attempts over three times and not successful are included (`FB`). Based on Baseball Savant's [Runner Basestealing](https://baseballsavant.mlb.com/leaderboard/basestealing-run-value).

**Examples**

```python
from baseball_stats_python import runner_basestealing

# Get Shohei Ohtani's runner basestealing data
runner_basestealing('660271')

# Get Shohei Ohtani's runner basestealing data in 2023
runner_basestealing('660271', season='2023')

# Get Shohei Ohtani's catcher throwing data in playoffs
catcher_throwing('660271', game_type=GameType.PLAYOFFS)
```

**Arguments**

| Argument             | Data Type           | Description                                                                                                                                                                                 |
| -------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| runner_id (Required) | `str`               | The MLBAM ID of the catcher.                                                                                                                                                                |
| game_type            | `str` or `GameType` | The game type to filter by. Can be `R` for regular season, `PO` for playoffs, or `All` for all games. Check enum [GameType](../enums/statcast_leaderboard.py)                               |
| season               | `str`               | The season to filter by. The earliest season available is 2016.                                                                                                                             |
| pitch_hand           | `str` or `Hand`     | The pitch hand to filter by. Default is "all". Check enum [Hand](../enums/statcast_leaderboard.py)                                                                                          |
| prior_pk             | `str`               | The number of prior pick-off attempts from pitcher before the stolen base opportunity. Default is "all". Can be "all", "1", "2", or "3". "3" is include all prior pick-off attempts over 3. |

**Return**

A DataFrame with columns that related to the [Runner Basestealing](https://baseballsavant.mlb.com/leaderboard/basestealing-run-value) leaderboard. The DataFrame will represent each stolen base attempt for a specific runner which contains data like `r_primary_lead`, `r_secondary_lead`, `run_value`, `r_sec_minus_prim_lead`, `runner_moved_cd`, etc.
