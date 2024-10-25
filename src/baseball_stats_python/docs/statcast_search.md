# Statcast Search

## statcast_search

Function to search for Statcast pitch-level data with custom filters based on Baseball Savant's [Statcast Search](https://baseballsavant.mlb.com/statcast_search).

**Notification:** If the search range is too wide, the response time will be very long.

**Examples**

```python
from baseball_stats_python import statcast_search

# Get Dodgers's pitcher data in July 2024
statcast_search(
    season="2024",
    team='LAD',
    player_type='pitcher',
    month="7"
)

# Get all pitch data in two days
statcast_search(
    start_dt="2024-07-01",
    end_dt="2024-07-02"
)

# Get all pitch data of a specific pitcher
# 669373 is Tarik Skubal's mlbam_id
statcast_search(
    pitchers_lookup="669373"
)

# Add debug=True to see more information
statcast_search(
    pitchers_lookup="669373",
    debug=True
)
```

**Arguments**

| Argument        | Data Type | Description                                                                                                                                                                | Default                                                                                                              |
| --------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| season          | `str      | list[str]`                                                                                                                                                                 | The season(s) to search for. Also support `all` to select all options and `statcast` to select all Statcast seasons. | Current season |
| player_type     | `str`     | Player type for search result. Currently only supports `pitcher` and `batter`.                                                                                             | "pitcher"                                                                                                            |
| game_type       | `str      | GameType                                                                                                                                                                   | list[str                                                                                                             | GameType]`     | Game type (`R`, `PO`, `F`, `D`, `L`, `W`, `S`, `A`). Can check enum [GameType](../enums/statcast.py). Also support `all` to select all options | `R` |
| start_dt        | `str`     | Start date (YYYY-MM-DD format)                                                                                                                                             | ""                                                                                                                   |
| end_dt          | `str`     | End date (YYYY-MM-DD format)                                                                                                                                               | ""                                                                                                                   |
| team            | `str      | MlbTeam                                                                                                                                                                    | list[str                                                                                                             | MlbTeam]`      | MLB team abbreviation(s) filter. Also support `all` to select all options. Can check enum [MlbTeam](../enums/statcast.py)                      | ""  |
| opponent        | `str      | MlbTeam                                                                                                                                                                    | list[str                                                                                                             | MlbTeam]`      | Opponent team abbreviation(s) filter. Also support `all` to select all options. Can check enum [MlbTeam](../enums/statcast.py)                 | ""  |
| pitchers_lookup | `str      | list[str]`                                                                                                                                                                 | Pitcher(s)'s mlbam_id                                                                                                | ""             |
| batters_lookup  | `str      | list[str]`                                                                                                                                                                 | Batter(s)'s mlbam_id                                                                                                 | ""             |
| month           | `str`     | Month (`4` - `9`). `4` would be March and April and `9` would be September and October. Also support `all` to select all options. Check enum [Month](../enums/statcast.py) | ""                                                                                                                   |
| debug           | `bool`    | Whether to print debug information                                                                                                                                         | False                                                                                                                |

**Use Enums**

```python
from baseball_stats_python.enums.statcast import GameType, MlbTeam

# Get Dodgers playoff data
statcast_search(
    game_type=GameType.PLAYOFF,
    team=MlbTeam.DODGERS
)
```

## statcast_pitcher_search

Based on `statcast_search`, but only returns pitcher data.

**Examples**

```python
from baseball_stats_python import statcast_pitcher_search

# Get all pitch data of a specific pitcher
statcast_pitcher_search(
    pitchers_lookup="669373"
)

# Can also search for multiple pitchers
statcast_pitcher_search(
    pitchers_lookup=["669373", "808967"]
)
```

**Arguments**

Same with `statcast_search` but only can use `pitchers_lookup` filter. If `pitchers_lookup` is not provided, it will throw an error.

## statcast_batter_search

Based on `statcast_search`, but only returns pitches that target batter faced.

**Examples**

```python
from baseball_stats_python import statcast_batter_search

# Get all pitch data of a specific batter
statcast_batter_search(
    batters_lookup="660271"
)

# Can also search for multiple batters
statcast_batter_search(
    batters_lookup=["660271", "592450"]
)
```

**Arguments**

Same with `statcast_search` but only can use `batters_lookup` filter. If `batters_lookup` is not provided, it will throw an error.
