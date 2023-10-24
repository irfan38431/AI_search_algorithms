# AI_search_algorithms# Pathfinding Algorithms in Python

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

### Depth-First Search (DFS)
DFS explores as far as possible along each branch before backtracking. It doesn't guarantee the shortest path, but it can be useful in certain scenarios.

### Best-First Search (BMS)
Best-First Search is an informed search algorithm that uses a heuristic to decide which adjacent node to explore next. It is not guaranteed to find the shortest path.

### A* Search
A* is a widely used pathfinding algorithm that uses both the cost to reach a node and a heuristic to estimate the cost from the current node to the goal. It ensures the shortest path and is often more efficient than BFS or DFS.

### Hill Climbing
Hill Climbing is a local search algorithm that continuously moves in the direction of increasing elevation/value to find the peak of the mountain (or the best solution). It can get stuck in local optima.

### Beam Search
Beam Search is a heuristic search algorithm that selects a limited set of paths to explore at each step. It's a balance between BFS and A*, providing a trade-off between optimality and computational resources.

## Usage

You can use these algorithms by importing the respective Python files into your project and creating instances of the algorithms classes. Each algorithm typically provides a method to find the shortest path between two nodes in a graph.

Example usage of A* algorithm:
```python
from astar import AStar

# Create a graph and add nodes and edges

# Instantiate the A* algorithm
astar = AStar(graph)

# Find the shortest path from start_node to goal_node
path = astar.find_path(start_node, goal_node)

print("Shortest path using A* algorithm:", path)
```

Feel free to contribute more search algorithms or improvements to the existing ones. Happy pathfinding! 🗺️
