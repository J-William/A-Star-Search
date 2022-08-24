from Problem import Problem as P

def solve(initial = [1, 2, 3, 4, 5, 6, 7, 0, 8], h = None):
    p = P(initial, h)
    root = p.Node(p.initial_state, None, None, 0)
    p.frontier.push((root.pathCost, root))

    while (p.frontier.size() > 0):
        # Get the next frontier node
        node = p.frontier.pop()
        # print("Popped from frontier: ", node)
        
        # print("Goal Test: {}".format(p.goal_test(node.state)))
        if p.goal_test(node.state):
            return p.solution(node)

        p.explored.add(node)

        for action in p.actions(node.state):
            child = p.create_child(node, action)
            # print(action, child)

            if (child not in p.explored) and (child.state not in p.frontier.array):
                # print('Pushed to frontier.')
                p.frontier.push((child.pathCost, child))
            elif (child.state in p.frontier.array):
                # Only replaces the entry if pathCost is higher
                # print('Replaced...?')
                p.frontier.replace(child)
        



if __name__ == '__main__':
    initial = input('Enter an initial state...')
    initial = [int(x) for x in initial.split(',')]

    answer = solve(initial)
    print(answer)