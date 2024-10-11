# baseball-stats-python

A package that get baseball data from

- [Baseball Savant](https://baseballsavant.mlb.com/)

## Overview

Inspired by [baseball-stats-python](https://github.com/ss77995ss/baseball-stats-python). This pacakge is mainly focused on getting pitch-by-pitch data from Baseball Data Website like Baseball Savant and provide a easy way to get data for analytics.

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

### statcast_search

Get pitch-by-pitch data from Baseball Savant with their search parameters.

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

## Contributing

Welcome to open issues or pull requests to contribute to this project. Please read [CONTRIBUTING.md](https://github.com/ss77995ss/baseball-stats-python/blob/main/CONTRIBUTING.md) for more details.

## License

[MIT License](https://github.com/ss77995ss/baseball-stats-python/blob/main/LICENSE)
