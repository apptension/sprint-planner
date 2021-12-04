from model.issue import Issue
from planner.algorithm.greedy_naive import GreedyNaive

def propose_schedule(calendar, issues):
    algorithm = GreedyNaive(calendar, issues)
    return algorithm.run()