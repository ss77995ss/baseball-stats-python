# Minor League Statcast Search

## minor_statcast_search

Function to search for Minor League Statcast pitch-level data with custom filters based on Baseball Savant's [Minor League Statcast Search](https://baseballsavant.mlb.com/statcast-search-minors).

**Notification:** If the search range is too wide, the response time will be very long.

**Minor League data availability**

> From Baseball Savant:
> Minor League Statcast tracking is available since the 2021 season for certain levels and ballparks. Data is available for:
>
> - All Triple-A games starting with the 2023 season, as well as Pacific Coast League games and Charlotte home games for the 2022 season
> - Florida State League (Single-A) games starting with the 2021 season

**Examples**

```python
from baseball_stats_python import minor_statcast_search

# Get all pitch data in July 2024
minor_statcast_search(
    month="7"
)

# Get all pitch data in two days
minor_statcast_search(
    start_dt="2024-07-01",
    end_dt="2024-07-02"
)

# Get all pitch data in Triple-A
minor_statcast_search(
    level="AAA"
)
```

**Arguments**

| Argument        | Data Type | Description                                                                                                                                                                | Default                                                                                             |
| --------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------ | --- |
| season          | `str      | list[str]`                                                                                                                                                                 | The season(s) to search for.                                                                        | Current season  |
| player_type     | `str`     | Player type for search result. Currently only supports `pitcher` and `batter`.                                                                                             | "pitcher"                                                                                           |
| game_type       | `str      | MinorGameType                                                                                                                                                              | list[str                                                                                            | MinorGameType]` | Game type (`R`, `PO`). Also support `all` to select all options. Can check enum [MinorGameType](../enums/minor.py) | `R` |
| start_dt        | `str`     | Start date (YYYY-MM-DD format)                                                                                                                                             | ""                                                                                                  |
| end_dt          | `str`     | End date (YYYY-MM-DD format)                                                                                                                                               | ""                                                                                                  |
| level           | `str      | Level`                                                                                                                                                                     | Minor League level. Currently only support `A` and `AAA`. Can check enum [Level](../enums/minor.py) | ""              |
| pitchers_lookup | `str      | list[str]`                                                                                                                                                                 | Pitcher(s)'s mlbam_id                                                                               | ""              |
| batters_lookup  | `str      | list[str]`                                                                                                                                                                 | Batter(s)'s mlbam_id                                                                                | ""              |
| month           | `str`     | Month (`4` - `9`). `4` would be March and April and `9` would be September and October. Also support `all` to select all options. Check enum [Month](../enums/statcast.py) | ""                                                                                                  |
| debug           | `bool`    | Whether to print debug information                                                                                                                                         | False                                                                                               |

**Use Enums**

```python
from baseball_stats_python.enums.minor import MinorGameType, Level

# Get playoff data
minor_statcast_search(
    game_type=MinorGameType.PLAYOFFS
)

# Get all pitch data in Triple-A using enum
minor_statcast_search(
    level=Level.AAA
)
```

## minor_statcast_pitcher_search

Based on `minor_statcast_search`, but only returns pitcher data.

**Examples**

```python
from baseball_stats_python import minor_statcast_pitcher_search

# Get all pitch data of a specific pitcher
minor_statcast_pitcher_search(
    pitchers_lookup="695549"
)
```

**Arguments**

Same with `minor_statcast_search` but only can use `pitchers_lookup` filter. If `pitchers_lookup` is not provided, it will throw an error.

## minor_statcast_batter_search

Based on `minor_statcast_search`, but only returns pitches that target batter faced.

**Examples**

```python
from baseball_stats_python import minor_statcast_batter_search

# Get all pitch data of a specific batter
minor_statcast_batter_search(
    batters_lookup="686611"
)
```

**Arguments**

Same with `minor_statcast_search` but only can use `batters_lookup` filter. If `batters_lookup` is not provided, it will throw an error.
