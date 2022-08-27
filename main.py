from Problem import Problem as P
from heuristics import mdist
from os import get_terminal_size
import random
import time


def generate_state(steps = 10):
    """ Generate a test state by taking a random walk from the goal state """
    p = P([0, 1, 2, 3, 4, 5, 6, 7, 8 ])
    state = p.initial_state
    for i in range(steps):
        action = random.choice(p.actions(state))
        state = p.result(state, action)
    return state


def solve(initial = [1, 0, 2, 3, 4, 5, 6, 7, 8], h = None):
    """ Algorithm implementation."""
    
    # Setup the problem and add the initial state node to the frontier.
    p = P(initial, h)
    root = p.Node(p.initial_state, None, None, 0)
    p.frontier.push((root.pathCost, root))

    while (p.frontier.size() > 0):
        # Get the next frontier node
        node = p.frontier.pop()
    
        if p.goal_test(node.state):
            return p.solution(node)

        p.explored.add(node)
        

        print(f"Solving from {p.initial_state} | Explored States: {len(p.explored)} | Frontier States: {len(p.frontier.array)}", end='\r')

        
        for action in p.actions(node.state):
            # Explore actions possible from this state; children of this node
            child = p.create_child(node, action)

            if (child not in p.explored) and (child not in p.frontier):
                # If the state has not been seen yet add it to the frontier to be explored
                p.frontier.push((child.pathCost, child))
            
            elif (child in p.frontier):
                # Only replaces the current entry with child if child has a lower path cost
                p.frontier.replace(child)


def timedSolve(state: P.State, heuristic = None):
    """ Wraps solve providing printout of details about the run."""
    tic = time.perf_counter()
    ans = solve(state.array, h=heuristic)
    toc = time.perf_counter()
    print('-'*100)
    print(f'Solved from initial state: {state}')
    print(f'Heuristic used: {str(heuristic)}')
    print(f'{len(ans)} moves in solution')
    print(f'Runtime: {toc-tic:0.4f} seconds.')
    print('-'*100)


if __name__ == '__main__':
    if get_terminal_size()[0] < 100:
        print('Warning: Increase the width of your terminal window for proper output.')
        input('Press enter to continue...')

    # Generate a few random states and test the algorithm with and without a heuristic
    states = [generate_state(x) for x in range(1, 50, 10)]
    
    for state in states:
        timedSolve(state)
        timedSolve(state, mdist)