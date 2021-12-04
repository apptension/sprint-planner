from model.issue import Issue
from planner.algorithm.greedy_naive import GreedyNaive

def propose_schedule(calendar, issues, time_per_estimation_point = None):
    algorithm = GreedyNaive(calendar, issues, time_per_estimation_point)
    return algorithm.run()