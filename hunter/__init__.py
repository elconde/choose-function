import itertools


def find_subsets(set_, size):
    """get all subsets of a given size of a set"""
    return list([set(x) for x in itertools.combinations(set_, size)])
