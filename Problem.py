from __future__ import annotations
from enum import Enum
import heapq


class Problem:
    """ 8x8 Sliding Block Puzzle Problem with Uniform Cost Search and A* Infrastructure"""
    def __init__(self, initial: list, heuristic: callable = None):
        # The set of explored states
        self.explored = set()
        # The frontier of states to explore ordered by path cost
        self.frontier = self.Frontier()
        # The initial state
        self.initial_state = self.State(initial)
        # If a heuristic function is provided it is used for A*
        self.h = heuristic

    @property
    def STEPCOST(self):
        """ CONSTANT - Uniform step cost of 1 for this problem"""
        return 1


    class State():
        """ Representation of a board state."""
        def __init__(self, init: list):
            # Only accept valid states
            if sorted(init) == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                self.array = init
            else:
                raise Exception('Invalid state creation attempt!')
        
        def __repr__(self) -> str:
            """ String representation."""
            out = str()
            for e in self.array:
                out += str(e)
            return "State({})".format(out)
        
        def __eq__(self,  other: object):
            """ Equality comparison"""
            if isinstance(other, Problem.State):
                return (self.array == other.array)
            else:
                return False
        
        def __ne__(self, other: object) -> bool:
            """ Inequality comparison"""
            return (not self.__eq__(other))

        def __hash__(self):
            """ Hash expression."""
            return hash(self.__repr__) 


    class Action(Enum):
        """ Enumeration of actions."""
        UP = 'UP'
        DOWN = 'DOWN'
        LEFT = 'LEFT'
        RIGHT = 'RIGHT'


    class Node(object):

        def __init__(self, state: Problem.State, parent: Problem.Node, action: Problem.Action, pathCost: int):
             # The state represented by the node
            self.state = state
            # The parent node that preceded this state
            self.parent = parent
            # The action that was taken from the parent state to get to this state
            self.action = action
            # The path cost of achieving this state from the initial state
            self.pathCost = pathCost

        def __repr__(self) -> str:
            """ Return a string representation of the node."""
            return self.state.__repr__() + " Action: {}, pathCost: {}".format(self.action, self.pathCost)

        def __eq__(self,  other: object):
            """ Equality comparison."""
            if isinstance(other, Problem.Node):
                return (self.state.array == other.state.array)
            else:
                return False
        
        def __ne__(self, other: object) -> bool:
            """ Inequality comparison."""
            return (not self.__eq__(other))
        
        def __lt__(self, other: object) -> bool:
            """ Less than comparison """
            if isinstance(other, Problem.Node):
                return (self.state.array < other.state.array)
            else:
                raise Exception("Can't compare Node with other objects.")

        def __gt__(self, other: object) -> bool:
            """ Greater than comparison """
            if isinstance(other, Problem.Node):
                return (self.state.array > other.state.array)
            else:
                raise Exception("Can't compare Node with other objects.")

        def __hash__(self) -> int:
            """ The hash for a node with a given state is the same as the hash for that state."""
            return hash(self.state.__repr__) 


    class Frontier():
        def __init__(self) -> None:
            """ Priority queue of tuple(pathCost, Node) order by min pathCost"""
            self.array = list()

        def __contains__(self, other: Problem.Node) -> bool:
            """ Compares by states of entries and the state of a target node."""
            for tup in self.array:
                if other.state == tup[1].state:
                    return True
            return False

        def size(self) -> int:
            return len(self.array)

        def replace(self, node: Problem.Node) -> None:
            """ Search the frontier for node with the same state but higher path cost; if found replace it."""
            for i in range(len(self.array)):
                if (self.array[i][1].state == node.state) and (self.array[i][0] > node.pathCost):
                    # Replace
                    self.array[i] = (node.pathCost, node)
            heapq.heapify(self.array)      

        def push(self, data: tuple[int, Problem.Node] ):
            heapq.heappush(self.array, data)
        
        def pop(self) -> Problem.Node:
            return heapq.heappop(self.array)[1]


    
    def actions(self, state: State) -> list:
        """ Returns a list of potential actions from a given state."""
        blank = state.array.index(0)

        if blank == 0:
            return [ self.Action.RIGHT, self.Action.DOWN ]
        elif blank == 1:
            return [ self.Action.LEFT, self.Action.RIGHT, self.Action.DOWN ]
        elif blank == 2:
            return [ self.Action.LEFT, self.Action.DOWN ]
        elif blank == 3:
            return [ self.Action.DOWN, self.Action.UP, self.Action.RIGHT ]
        elif blank == 4:
            return [ self.Action.DOWN, self.Action.UP, self.Action.RIGHT, self.Action.LEFT ]    
        elif blank == 5:
            return [ self.Action.LEFT, self.Action.UP, self.Action.DOWN ]
        elif blank == 6:
            return [ self.Action.UP, self.Action.RIGHT ]
        elif blank == 7:
            return [ self.Action.LEFT, self.Action.RIGHT, self.Action.UP ]
        elif blank == 8:
            return [ self.Action.LEFT, self.Action.UP ]
        else:
            raise Exception('State index error resolving potential actions.')


    def heuristic(self, state: State) -> int:
        """ 
            Map any supplied heuristic function to the create_child's 
            pathCost evaluation. Returns 0 if a function is not supplied so that the
            pathCost formula: (parent.pathCost + STEPCOST + heuristic(newNode.state))
            is unaffected.         
        """
        if self.h:
            return self.h(state)
        else:
            return 0


    def result(self, state: State, action: Action) -> list:
        """ Return the new state resulting from an action on a given state."""
        blank = state.array.index(0)
        
        # Determine the location of the block to swap with based on action
        if action == self.Action.UP:
            target = blank - 3
        elif action == self.Action.LEFT:
            target = blank - 1
        elif action == self.Action.RIGHT:
            target = blank + 1
        elif action == self.Action.DOWN:
            target = blank + 3
        else:
            raise Exception('Invalid Action attempted.')    

        # Create the new result state as a copy of parent
        newState = self.State(state.array.copy())
        # Swap the location of the target block and the blank to get the new state
        newState.array[blank], newState.array[target] = newState.array[target], newState.array[blank]
        return newState    

    def create_child(self, parent: Node, action: Action):
        """ Create a child node from the parent and an action."""        
        newState = self.result(parent.state, action)

        return self.Node(
            state   =    newState,
            parent  =    parent,
            action  =    action,
            pathCost =  parent.pathCost + self.STEPCOST + self.heuristic(newState)

        )


    def goal_test(self, state: State) -> bool:
        """ Test for the goal state. """
        return state.array == sorted(state.array)


    def solution(self, node: Node) -> list:
        """ Generate a solution when a goal state is reached."""
        actions = list()
        while(node.parent is not None):
            actions.append(node.action)
            node = node.parent
        
        actions.reverse()
        return actions