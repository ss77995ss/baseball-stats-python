# MLBAM ID Search

## `mlbam_id_search`

Function to search for MLBAM IDs by player's name. It will return a DataFrame with the player's name, MLBAM ID, and other information. Would not need to use full name to search. The function will get the most relevant result and return at most 10 results. Users can use the `id` to search for the player in other functions like `statcast_search`.

**Examples**

```python
from baseball_stats_python import mlbam_id_search

# Get MLBAM IDs with name similar to "Reynolds"
mlbam_id_search('Reynolds')

# Get Yadier Molina's MLBAM ID
mlbam_id_search('Molina').iloc[0]['id']
```

**Arguments**

| Argument               | Data Type | Description                                                                     |
| ---------------------- | --------- | ------------------------------------------------------------------------------- |
| player_name (Required) | `str`     | Player's name that would be used to search for MLBAM ID. Can be a partial name. |
| debug                  | `bool`    | If `True`, print out the search query. Default is `False`.                      |

**Return**

A DataFrame with the following columns:

- `name`: Player's name
- `id`: MLBAM ID
- `pos`: Player's position
- `last_year`: The year the player last played in MLB
