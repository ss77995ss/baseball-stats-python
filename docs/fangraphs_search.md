# Fangraphs Search

## `fangraphs_search`

Function to get leaderboard data from the Fangraphs [major-league leaders API](https://www.fangraphs.com/leaders/major-league) with custom filters. The `stats` argument selects the batting (`bat`) or pitching (`pit`) leaderboard.

**Notification:** Not all argument descriptions are fully verified against the Fangraphs API yet.

**Examples**

```python
from baseball_stats_python import fangraphs_search

# Get the 2026 qualified batting leaderboard
fangraphs_search(
    stats="bat",
    season=2026
)

# Get the qualified pitching leaderboard across multiple seasons (2024-2026)
fangraphs_search(
    stats="pit",
    season1=2024,
    season=2026
)

# Filter by a date range (set month=1000 to activate the date filter)
fangraphs_search(
    stats="bat",
    month=1000,
    start_date="2026-04-01",
    end_date="2026-04-30"
)

# Add debug=True to see more information
fangraphs_search(
    stats="bat",
    debug=True
)
```

**Arguments**

| Argument    | Data Type      | Description                                                                                            | Default        |
| ----------- | -------------- | ----------------------------------------------------------------------------------------------------- | -------------- |
| stats       | `str`          | Stat group to fetch — `bat` for batting or `pit` for pitching.                                        | "bat"          |
| age         | `int`          | Filter by player age. `0` means no age filter.                                                        | 0              |
| pos         | `str`          | Position filter (e.g. `all`, `c`, `1b`, `of`, `np` for non-pitchers).                                 | "all"          |
| lg          | `str`          | League filter — `all`, `al`, or `nl`.                                                                 | "all"          |
| qual        | `int` or `str` | Plate-appearance/innings qualifier. `y` for the qualified threshold, an integer for a custom minimum, or `0` for no minimum. | "y"            |
| season      | `int`          | End season of the range to query.                                                                     | Current season |
| season1     | `int`          | Start season of the range. Equals `season` for a single season.                                       | Current season |
| start_date  | `str`          | Range start date in `YYYY-MM-DD` format (set `month=1000` to activate this filter).                   | "2026-03-01"   |
| end_date    | `str`          | Range end date in `YYYY-MM-DD` format (set `month=1000` to activate this filter).                     | "2026-11-01"   |
| month       | `int`          | Split by calendar month/period. `0` means full season. `1000` means use `start_date`/`end_date`.      | 0              |
| hand        | `str`          | Batter/pitcher handedness filter — `R`, `L`, or `""` for both.                                        | ""             |
| team        | `str`          | Team filter by Fangraphs team id; `""` means all teams.                                               | ""             |
| pageitems   | `int`          | Number of rows per page. Default is high enough to return all rows.                                   | 10000          |
| pagenum     | `int`          | Page number to fetch.                                                                                 | 1              |
| ind         | `int`          | Split seasons individually (`1`) or aggregate the range into one row (`0`).                           | 0              |
| rost        | `int`          | Roster filter — `0` for all players, `1` for active roster only.                                      | 0              |
| players     | `str`          | Filter to specific player id(s); `""` means all players.                                              | ""             |
| type        | `int`          | Stat dashboard/column set id (`8` is the default dashboard).                                          | 8              |
| postseason  | `str`          | Set to a truthy value to query postseason stats; `""` for regular season.                             | ""             |
| heatmapqual | `str`          | Heatmap qualifier flag passed through to the API.                                                     | ""             |
| sortdir     | `str`          | Sort direction — `default`, `asc`, or `desc`.                                                         | "default"      |
| sortstat    | `str`          | Column to sort by (e.g. `WAR`).                                                                       | "WAR"          |
| debug       | `bool`         | Whether to print debug information (request params and URL).                                          | False          |

**Return**

A DataFrame of the leaderboard rows, with HTML stripped from the `Name` and `Team` columns. An empty DataFrame is returned when the API has no matching data.

## `fg_batting`

Convenience wrapper around `fangraphs_search` with `stats="bat"`. Currently only supports single-season queries — use `fangraphs_search` for multi-season queries.

**Examples**

```python
from baseball_stats_python import fg_batting

# Get the 2026 qualified batting leaderboard
fg_batting(season=2026)

# Use a custom plate-appearance minimum instead of the qualified threshold
fg_batting(qual=100, season=2026)
```

**Arguments**

| Argument | Data Type      | Description                                                                                          | Default        |
| -------- | -------------- | --------------------------------------------------------------------------------------------------- | -------------- |
| qual     | `int` or `str` | Plate-appearance qualifier — `y` for the qualified threshold, an integer for a custom minimum, or `0` for no minimum. | 0              |
| season   | `int`          | Season to query.                                                                                    | Current season |
| debug    | `bool`         | Whether to print debug information.                                                                 | False          |

## `fg_pitching`

Convenience wrapper around `fangraphs_search` with `stats="pit"`. Currently only supports single-season queries — use `fangraphs_search` for multi-season queries.

**Examples**

```python
from baseball_stats_python import fg_pitching

# Get the 2026 qualified pitching leaderboard
fg_pitching(season=2026)

# Use a custom innings-pitched minimum instead of the qualified threshold
fg_pitching(qual=50, season=2026)
```

**Arguments**

| Argument | Data Type      | Description                                                                                          | Default        |
| -------- | -------------- | --------------------------------------------------------------------------------------------------- | -------------- |
| qual     | `int` or `str` | Innings-pitched qualifier — `y` for the qualified threshold, an integer for a custom minimum, or `0` for no minimum. | 0              |
| season   | `int`          | Season to query.                                                                                    | Current season |
| debug    | `bool`         | Whether to print debug information.                                                                 | False          |
