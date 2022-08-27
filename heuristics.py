from Problem import Problem

def manhattan_distance(point1, point2) -> int:
    """ Returns the manhattan distance between two locations on the 8-Block board."""
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def mdist(state: Problem.State|list[int]):
    """ Return a summation of the manhattan distances between blocks and their home."""    
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
        dist += manhattan_distance((homex, homey), (block[1], block[2]))

    return dist  
