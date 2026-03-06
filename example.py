"""Example usage of the baseball_stats_python package."""

from src.baseball_stats_python import (
    minor_statcast_search,
    mlbam_id_search,
    statcast_search,
    wbc_statcast_search,
)
from src.baseball_stats_python.enums.minor import MinorGameType
from src.baseball_stats_python.enums.statcast import GameType, MlbTeam, Month


def example():
    df = statcast_search(
        season="2023",
        pitchers_lookup="477132",
        game_type=[GameType.PLAYOFFS, "R"],
        opponent=MlbTeam.PADRES,
        month=Month.JUNE,
    )
    print(df)


def minor_example():
    df = minor_statcast_search(
        season="2023", game_type=MinorGameType.REGULAR_SEASON, pitchers_lookup="678906"
    )
    print(df)


def mlbam_id_example():
    df = mlbam_id_search("Lin")
    print(df)


def spring_training_example():
    df = statcast_search(
        season="2025",
        start_dt="2025-02-20",
        end_dt="2025-02-20",
        game_type="S",
    )
    print(df)


def wbc_example():
    df = wbc_statcast_search(
        batters_lookup="838360",
    )
    print(df)


# example()
# minor_example()
# mlbam_id_example()
# spring_training_example()
# wbc_example()
