from Problem import Problem as P
from heuristics import mdist
import random
import time


def generate_state(iterations = 10):
    """ Generate a test state a certain number of random actions from the goal state."""
    p = P([0, 1, 2, 3, 4, 5, 6, 7, 8 ])
    state = p.initial_state
    for i in range(iterations):
        action = random.choice(p.actions(state))
        state = p.result(state, action)
    return state


def solve(initial = [1, 0, 2, 3, 4, 5, 6, 7, 8], h = None):
    """ Algorithm implementation."""
    p = P(initial, h)
    root = p.Node(p.initial_state, None, None, 0)
    p.frontier.push((root.pathCost, root))

    while (p.frontier.size() > 0):
        # Get the next frontier node
        node = p.frontier.pop()
    
        if p.goal_test(node.state):
            return p.solution(node)

        p.explored.add(node)
        print(f'Explored {len(p.explored)} | Frontier Size: {len(p.frontier.array)}', end='\r')
        

        for action in p.actions(node.state):
            child = p.create_child(node, action)

            if (child not in p.explored) and (child not in p.frontier):
                p.frontier.push((child.pathCost, child))
            
            elif (child in p.frontier):
                # Only replaces the entry if pathCost is higher
                p.frontier.replace(child)        


def timedSolve(state: P.State, heuristic = None):
    """ Wraps solve providing printout of details about the run."""
    tic = time.perf_counter()
    ans = solve(state.array, h=heuristic)
    toc = time.perf_counter()

    print(f'From initial state: {state}')
    print(f'Heuristic used: {str(heuristic != None)}')
    print(f'{len(ans)} moves in solution')
    print(f'Runtime: {toc-tic:0.4f} seconds.')
    print('-'*50, flush=True)


if __name__ == '__main__':
    # Generate a few random states and test the algorithm with and without a heuristic
    states = [generate_state(x) for x in range(1, 50, 10)]
    
    for state in states:
        timedSolve(state)
        timedSolve(state, mdist)