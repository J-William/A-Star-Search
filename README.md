# A* Search

An algorithm to solve 8x8 [Sliding Block puzzles](https://en.wikipedia.org/wiki/Sliding_puzzle) with Uniform Cost Search and A* Search.

By defaul the algorithm is a Uniform Cost search, if a heuristic function is supplied it is used in the 
Path Cost calculation for new Nodes and the algorithm becomes an A* Search.


|Files||
|--------------|:----------------------:|
| Problem.py | The Problem class provides all the search problem infrastructure.|
|heuristics.py| Provides manahattan and euclidean distance functions for use with A*.|
|main.py|Contains the implementation of the algorithm and demonstration/testing routines.|

