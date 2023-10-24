Certainly! Here's an updated version of the README.md file with example usages for each implemented search algorithm:

# Pathfinding Algorithms in Python

This repository contains implementations of various search algorithms in Python. These algorithms are dedicated to finding paths from one node to another in a graph. Currently implemented algorithms include:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Best-First Search (BMS)**
- **A* Search**
- **Hill Climbing**
- **Beam Search**

## Algorithms Overview

### Breadth-First Search (BFS)
BFS explores all the neighbor nodes at the present depth prior to moving on to nodes at the next depth level. It guarantees the shortest path from the start node to every other node in an unweighted graph.

**Example Usage:**
```python
from bfs import BFS

# Create a graph and add nodes and edges

# Instantiate the BFS algorithm
bfs = BFS(graph)

# Find the shortest path from start_node to goal_node
path = bfs.find_path(start_node, goal_node)

print("Shortest path using BFS algorithm:", path)
```

### Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking. It doesn't guarantee the shortest path, but it can be useful in certain scenarios.

**Example Usage:**
```python
from dfs import DFS

# Create a graph and add nodes and edges

# Instantiate the DFS algorithm
dfs = DFS(graph)

# Find the path from start_node to goal_node
path = dfs.find_path(start_node, goal_node)

print("Path using DFS algorithm:", path)
```

### Best-First Search (BMS)
Best-First Search is an informed search algorithm that uses a heuristic to decide which adjacent node to explore next. It is not guaranteed to find the shortest path.

**Example Usage:**
```python
from best_first_search import BestFirstSearch

# Create a graph and add nodes and edges

# Instantiate the Best-First Search algorithm with a heuristic function
bms = BestFirstSearch(graph, heuristic_function)

# Find the path from start_node to goal_node
path = bms.find_path(start_node, goal_node)

print("Path using Best-First Search algorithm:", path)
```

### A* Search
A* is a widely used pathfinding algorithm that uses both the cost to reach a node and a heuristic to estimate the cost from the current node to the goal. It ensures the shortest path and is often more efficient than BFS or DFS.

**Example Usage:**
```python
from astar import AStar

# Create a graph and add nodes and edges

# Instantiate the A* algorithm
astar = AStar(graph)

# Find the shortest path from start_node to goal_node
path = astar.find_path(start_node, goal_node)

print("Shortest path using A* algorithm:", path)
```

### Hill Climbing
Hill Climbing is a local search algorithm that continuously moves in the direction of increasing elevation/value to find the peak of the mountain (or the best solution). It can get stuck in local optima.

**Example Usage:**
```python
from hill_climbing import HillClimbing

# Create a problem instance

# Instantiate the Hill Climbing algorithm
hill_climbing = HillClimbing(problem_instance)

# Find the best solution
best_solution = hill_climbing.find_solution()

print("Best solution using Hill Climbing algorithm:", best_solution)
```

### Beam Search
Beam Search is a heuristic search algorithm that selects a limited set of paths to explore at each step. It's a balance between BFS and A*, providing a trade-off between optimality and computational resources.

**Example Usage:**
```python
from beam_search import BeamSearch

# Create a graph and add nodes and edges

# Instantiate the Beam Search algorithm with a beam width
beam_search = BeamSearch(graph, beam_width)

# Find the path from start_node to goal_node
path = beam_search.find_path(start_node, goal_node)

print("Path using Beam Search algorithm:", path)
```

Feel free to use these algorithms in your projects and contribute more search algorithms or improvements to the existing ones. Happy pathfinding! 🗺️
