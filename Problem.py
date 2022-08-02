from __future__ import annotations
from enum import Enum
from queue import PriorityQueue

class Problem:

    def __init__(self, initial_state: list):
        # The set of explored states
        self.explored = set()
        # Uniform step cost for this problem
        self._STEPCOST = 1
        # The frontier of states to explore order by path cost
        self.frontier = PriorityQueue()
        # The initial state
        self.initial_state = initial_state

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
            out = str()
            for e in self.state:
                out += str(e)
            return "State({})".format(out)

        def __eq__(self,  other: object):
            if isinstance(other, Problem.Node):
                return (self.state == other.state)
            else:
                return False
        
        def __ne__(self, other: object) -> bool:
            return (not self.__eq__(other))
        
        def __hash__(self) -> int:
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
        mdist = 0
        from mdist import manhattan_distance

        for e in state:
            location = state.index(e)        
            # Any given block's home index is 1 less than itself.
            home = e - 1
            mdist += manhattan_distance(location, home)
        
        return mdist


    def create_child(self, parent: Node, action: Action):
        """ Create a child node from the parent and an action."""        
        pass
