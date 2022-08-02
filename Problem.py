from __future__ import annotations
from enum import Enum
from queue import PriorityQueue

class Problem:

    def __init__(self, initial_state: list, heuristic = None):
        # The set of explored states
        self.explored = set()
        # Uniform step cost for this problem
        self._STEPCOST = 1
        # The frontier of states to explore order by path cost
        self.frontier = PriorityQueue()
        # The initial state
        self.initial_state = initial_state
        # The heuristic funciton to use
        self.h = heuristic

    class Action(Enum):
        """ Enumeration of actions."""
        UP = 'UP'
        DOWN = 'DOWN'
        LEFT = 'LEFT'
        RIGHT = 'RIGHT'

    class Node(object):

        def __init__(self, state: list, parent: Problem.Node, action: Problem.Action, pathCost: int):
             # The state represented by the node
            self.state = state
            # The parent node that preceded this state
            self.parent = parent
            # The action that was taken from the parent state to get to this state
            self.action = action
            # The path cost of achieving this state from the initial state
            self.pathCost = pathCost

        def __repr__(self) -> str:
            """ Return a string representation of the node's state."""
            out = str()
            for e in self.state:
                out += str(e)
            return "State({})".format(out)

        def __eq__(self,  other: object):
            """ Equality comparison."""
            if isinstance(other, Problem.Node):
                return (self.state == other.state)
            else:
                return False
        
        def __ne__(self, other: object) -> bool:
            """ Inequality comparison."""
            return (not self.__eq__(other))
        
        def __hash__(self) -> int:
            """ Hash function necessary to add to a Set."""
            return hash(self.__repr__) 


    
    def actions(self, state: list) -> list:
        """ Returns a list of potential actions from a given state."""
        blank = state.index(0)

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

    def heuristic(self, state: list) -> int:
        """ 
            Returns a heuristic measure of a state's undesirability given by the sum of the 
            direct step distances between each block and it's goal location.
        """
        if self.h:
            return self.h(state)
        else:
            return 0


    def result(self, state: list, action: Action) -> list:
        """ Return the new state resulting from an action on a given state."""
        blank = state.index(0)
        
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

        # Swap the location of the target block and the blank
        state[blank], state[target] = state[target], state[blank]
        return state    

    def create_child(self, parent: Node, action: Action):
        """ Create a child node from the parent and an action."""        
        pass