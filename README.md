# baseball-stats-python

A package that get baseball data from

- [Baseball Savant](https://baseballsavant.mlb.com/)

## Overview

Inspired by [pybaseball](https://github.com/jldbc/pybaseball). This pacakge is mainly focused on getting pitch-by-pitch data from Baseball Data Website like Baseball Savant and provide a easy way to get data for analytics.

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

Get pitch-by-pitch data from Baseball Savant with their search parameters. See documentation [here](src/baseball_stats_python/docs/statcast_search.md).

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

Get pitch-by-pitch data from Baseball Savant's Minor League Statcast Search with their search parameters. See documentation [here](src/baseball_stats_python/docs/minor_statcast_search.md).

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

Search for MLBAM ID(s) by player name. Can be used to get player ID for `statcast_batter_search` and `statcast_pitcher_search`. See documentation [here](src/baseball_stats_python/docs/mlbam_id_search.md).

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

## Contributing

Welcome to open issues or pull requests to contribute to this project. Please read [CONTRIBUTING.md](https://github.com/ss77995ss/baseball-stats-python/blob/main/CONTRIBUTING.md) for more details.

## License

[MIT License](https://github.com/ss77995ss/baseball-stats-python/blob/main/LICENSE)
