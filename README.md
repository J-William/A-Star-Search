# A* Search

An algorithm to solve 8x8 [Sliding Block puzzles](https://en.wikipedia.org/wiki/Sliding_puzzle) with Uniform Cost Search and A* Search.

By defaul the algorithm is a Uniform Cost search, if a heuristic function is supplied it is used in the Path Cost calculation for new Nodes and the algorithm becomes an A* Search. For this puzzle the board state is represented by a list of integers where 0 represents the missing block that allows for sliding such that `[ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]` is the goal state.

##### An 8x8 Block board in the goal state
<table>
  <tr>
    <td>0</td><td>1</td><td>2</td>
  </tr>
  <tr>
    <td>3</td><td>4</td><td>5</td>
  </tr>
  <tr>
    <td>6</td><td>7</td><td>8</td>
  </tr>
</table>


<br>
<br>

|Files||
|-----|------|
| Problem.py | The Problem class provides all the search problem infrastructure.|
|heuristics.py| Provides manahattan and euclidean distance functions for use with A*.|
|main.py|Contains the implementation of the algorithm and demonstration/testing routines.|

<br>
<br>

##### A basic interface is included for demonstration/testing
![image](https://user-images.githubusercontent.com/21013517/187051887-201ca545-0573-4f8b-8bb1-c22a3ccb3b0f.png)

<br>
<br>

##### How to run
Standard Python 3.10 or greater is required
<br>
Clone the repo locally and execute `python main.py` or `python3 main.py` depending on how your environment is configured.

