"""Example usage of the baseball_stats_python package."""

from src.baseball_stats_python.statcast.statcast_search import statcast_search


def example():
    df = statcast_search(pitchers_lookup="477132")
    print(df)


example()
