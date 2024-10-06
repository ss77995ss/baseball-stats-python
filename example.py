"""Example usage of the baseball_stats_python package."""

from src.baseball_stats_python import statcast_search
from src.baseball_stats_python.enums.statcast import MlbTeam, GameType, Month


def example():
    df = statcast_search(season="2023", pitchers_lookup="477132",
                         game_type=[GameType.PLAYOFFS, "R"], opponent=MlbTeam.PADRES, month=Month.JUNE)
    print(df)


example()
