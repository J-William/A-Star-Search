from Problem import Problem
from math import sqrt


def evaluate_over_board(state: Problem.State, measure: callable) -> int:
    """ Sums the values returned by a given heuristic distiance meausre between all blocks and their homes."""
    matrix = list()
    dist = int()
    i = 0
    for x in range(1, 4):
        for y in range(1, 4):
            # Matrix of tuple(val, x, y)
            matrix.append((state.array[i], x, y))
            i += 1
    
    for block in matrix:
        # The blocks home index is its value: tuple(val, x, y)
        homex, homey = matrix[block[0]][1], matrix[block[0]][2]
        dist += measure((homex, homey), (block[1], block[2]))

    return dist  


def mdist(point1, point2) -> int:
    """ Returns the manhattan distance between two points."""
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def edist(point1, point2)  -> int:
    """ Returns the euclidean distance between two points."""
    return sqrt(pow((point1[0] - point2[0]), 2) + pow((point1[1] - point2[1]), 2))


def manhattan_distance(state: Problem.State) -> int:
    """ Return a summation of the manhattan distances between blocks and their home."""    
    return evaluate_over_board(state, mdist)

def euclidean_distance(state: Problem.State) -> int:
    """ Return a summation of the euclidean distance between block and their home."""
    return evaluate_over_board(state, edist)
