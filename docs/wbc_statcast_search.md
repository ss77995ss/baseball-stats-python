# WBC Statcast Search

## `wbc_statcast_search`

Function to search for WBC Statcast pitch-level data with custom filters based on Baseball Savant's [WBC Statcast Search](https://baseballsavant.mlb.com/statcast-search-world-baseball-classic).

**Notification:** If the search range is too wide, the response time will be very long.

**WBC data availability**

> From Baseball Savant:
> World Baseball Classic pitch-level Statcast data is available beginning with the 2023 tournament. Bat tracking data will additionally be available beginning with the 2026 tournament.

**Examples**

```python
from baseball_stats_python import wbc_statcast_search

# Get all pitch data in 2023 WBC
wbc_statcast_search(
    season="2023"
)

# Get all pitch data in 2026 Pool Play
wbc_statcast_search(
    game_type="F"
)
```

**Arguments**

| Argument        | Data Type                                                | Description                                                                                                                                                                | Default        |
| --------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| season          | `str` or `list[str]`                                     | The season(s) to search for.                                                                                                                                               | Current season |
| player_type     | `str`                                                    | Player type for search result. Currently only supports `pitcher` and `batter`.                                                                                             | "pitcher"      |
| game_type       | `str` or `WbcGameType` or `list[str or WbcGameType]` | Game type (`F`, `CL`, `CD`, `CW`). Also support `all` to select all options. Can check enum [WbcGameType](../enums/wbc.py)                                                         | `R`            |
| pitchers_lookup | `str` or `list[str]`                                     | Pitcher(s)'s mlbam_id. Can get MLBAM ID from Savant's WBC gameday                                                                                       | ""             |
| batters_lookup  | `str` or `list[str]`                                     | Batter(s)'s mlbam_id. Can get MLBAM ID from Savant's WBC gameday                                                                                        | ""             |
| debug           | `bool`                                                   | Whether to print debug information                                                                                                                                         | False          |

**Use Enums**

```python
from baseball_stats_python.enums.minor import WbcGameType

# Get Semi-Finals data
wbc_statcast_search(
    game_type=WbcGameType.SEMI_FINALS
)

```

**Return**

A DataFrame with columns can be found from Baseball Savant's [CSV Docs](https://baseballsavant.mlb.com/csv-docs).

## `wbc_statcast_pitcher_search`

Based on `wbc_statcast_search`, but only returns pitcher data.

**Examples**

```python
from baseball_stats_python import wbc_statcast_pitcher_search

# Get all pitch data of a specific pitcher
wbc_statcast_pitcher_search(
    pitchers_lookup="830717"
)
```

**Arguments**

Same with `wbc_statcast_search` but only can use `pitchers_lookup` filter. If `pitchers_lookup` is not provided, it will throw an error.

## `wbc_statcast_batter_search`

Based on `wbc_statcast_search`, but only returns pitches that target batter faced.

**Examples**

```python
from baseball_stats_python import wbc_statcast_batter_search

# Get all pitch data of a specific batter
wbc_statcast_batter_search(
    batters_lookup="838360"
)
```

**Arguments**

Same with `wbc_statcast_batter_search` but only can use `batters_lookup` filter. If `batters_lookup` is not provided, it will throw an error.
