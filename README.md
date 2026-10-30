# baseball-stats-python

A package that get baseball data from

- [Baseball Savant](https://baseballsavant.mlb.com/)
- [FanGraphs Leaderboard](https://www.fangraphs.com/leaders/major-league)

## Overview

Inspired by [pybaseball](https://github.com/jldbc/pybaseball). This pacakge is mainly focused on getting pitch-by-pitch data from Baseball Data Website like Baseball Savant and provide a easy way to get data for analytics. All credit belong to the data source's organziations.

## Installation

Install the package via pip

```bash
pip install baseball-stats-python
```

Download the main branch by `git clone`

```bash
git clone https://github.com/ss77995ss/baseball-stats-python.git
```

pip with repository url

```bash
pip install git+https://github.com/ss77995ss/baseball-stats-python.git
```

## Usage

#### `statcast_search`

Get pitch-by-pitch data from Baseball Savant with their search parameters. See documentation [here](docs/statcast_search.md).

```python
from baseball_stats_python import statcast_search

# Get Dodgers's pitcher data in July 2024
statcast_search(
    season="2024",
    team='LAD',
    player_type='pitcher',
    month="7"
)
```

#### `minor_statcast_search`

Get pitch-by-pitch data from Baseball Savant's Minor League Statcast Search with their search parameters. See documentation [here](docs/minor_statcast_search.md).

```python
from baseball_stats_python import minor_statcast_search

# Get all pitch data in Triple-A in July 2024
minor_statcast_search(
    season="2024",
    level="AAA",
    month="7"
)
```

#### `mlbam_id_search`

Search for MLBAM ID(s) by player name. Can be used to get player ID for `statcast_batter_search` and `statcast_pitcher_search`. See documentation [here](docs/mlbam_id_search.md).

```python
from baseball_stats_python import (
    mlbam_id_search,
    statcast_batter_search,
    statcast_pitcher_search,
)

# Search for MLBAM ID(s) by player name
molina_mlbam_id = mlbam_id_search('Yadier Molina').iloc[0]['id']

# Get Yadier Molina's Statcast data
statcast_batter_search(batters_lookup=mlbam_id)

darvish_mlbam_id = mlbam_id_search('Yu Darvish').iloc[0]['id']

# Get Yu Darvish's Statcast data
statcast_pitcher_search(pitchers_lookup=darvish_mlbam_id)
```

#### `fangraphs_search`

Get batting or pitching leaderboard data from Fangraphs' [major-league leaders API](https://www.fangraphs.com/leaders/major-league). `fg_batting` and `fg_pitching` are convenience wrappers for single-season queries. See documentation [here](docs/fangraphs_search.md).

```python
from baseball_stats_python import fangraphs_search, fg_batting, fg_pitching

# Get the 2026 qualified batting leaderboard
fg_batting(season=2026)

# Get the 2026 qualified pitching leaderboard
fg_pitching(season=2026)

# Use fangraphs_search directly for multi-season or finer-grained queries
fangraphs_search(
    stats="bat",
    season1=2024,
    season=2026
)
```

### Request timeouts

Every request has a timeout, so a slow or unresponsive server raises an error instead of hanging. Statcast CSV searches get a longer read timeout than the other endpoints. Adjust them in seconds:

```python
from baseball_stats_python import set_request_timeout

set_request_timeout(search_read=300)  # allow slower Statcast searches
```

### Errors and logging

Failed requests raise `RequestError` (with `status_code` and `url`); a source that does not answer in time raises `RequestTimeoutError`. Both inherit from `BaseballStatsError`, so one `except` catches everything the package raises on purpose. Invalid arguments still raise `ValueError`.

```python
from baseball_stats_python import RequestTimeoutError, statcast_search

try:
    df = statcast_search(season=2025)
except RequestTimeoutError:
    df = statcast_search(season=2025, start_dt="2025-04-01", end_dt="2025-04-30")
```

The package logs instead of printing. To see progress messages:

```python
import logging

logging.basicConfig(level=logging.INFO)
```

Pass `debug=True` to any function to print request details for this package only.

## Contributing

Welcome to open issues or pull requests to contribute to this project. Please read [CONTRIBUTING.md](https://github.com/ss77995ss/baseball-stats-python/blob/main/CONTRIBUTING.md) for more details.

## License

[MIT License](https://github.com/ss77995ss/baseball-stats-python/blob/main/LICENSE)
