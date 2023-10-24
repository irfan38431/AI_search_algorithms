from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, target, visited, path, shortest_path):
        visited[node] = True
        path.append(node)

        if node == target:
            if len(shortest_path) == 0 or len(path) < len(shortest_path):
                shortest_path[:] = path[:]
        else:
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    self.dfs(neighbor, target, visited, path, shortest_path)

        path.pop()
        visited[node] = False

def shortest_path(graph, start, target, num_nodes):
    visited = [False] * num_nodes
    path = []
    shortest_path = []
    graph.dfs(start, target, visited, path, shortest_path)
    return shortest_path

# Example usage
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(2, 6)

start_node = 0
target_node = 4
num_nodes = 7  # Total number of nodes in the graph
result = shortest_path(graph, start_node, target_node, num_nodes)

if len(result) > 0:
    print(f"Shortest path from {start_node} to {target_node}: {result}")
else:
    print(f"No path found from {start_node} to {target_node}")
