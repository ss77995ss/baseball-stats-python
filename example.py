"""Example usage of the baseball_stats_python package."""

from src.baseball_stats_python import minor_statcast_search, statcast_search
from src.baseball_stats_python.enums.minor import MinorGameType
from src.baseball_stats_python.enums.statcast import GameType, MlbTeam, Month


def example():
    df = statcast_search(
        season='2023',
        pitchers_lookup='477132',
        game_type=[GameType.PLAYOFFS, 'R'],
        opponent=MlbTeam.PADRES,
        month=Month.JUNE,
    )
    print(df)


def minor_example():
    df = minor_statcast_search(
        season='2023', game_type=MinorGameType.REGULAR_SEASON, pitchers_lookup='678906'
    )
    print(df)


# example()
# minor_example()
