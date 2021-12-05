from enum import Enum
from model.issue import Issue
from planner.algorithm.greedy_naive import GreedyNaive
from planner.algorithm.greedy_naive_with_split import GreedyNaiveWithSplit


class Algorithm(Enum):
    NAIVE_GREEDY = (1,)
    NAIVE_GREEDY_WITH_SPLIT = 2


def propose_schedule(
    schedule, issues, time_per_estimation_point=None, algorithm=Algorithm.NAIVE_GREEDY
):
    print(algorithm)
    algorithm = {
        Algorithm.NAIVE_GREEDY: GreedyNaive,
        Algorithm.NAIVE_GREEDY_WITH_SPLIT: GreedyNaiveWithSplit,
    }[algorithm](schedule, issues, time_per_estimation_point)

    return algorithm.run()
