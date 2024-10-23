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
