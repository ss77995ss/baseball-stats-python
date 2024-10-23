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
