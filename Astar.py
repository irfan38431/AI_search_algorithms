import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
    
    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []
    
    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node].append((to_node, cost))
        self.edges[to_node].append((from_node, cost))

def astar(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.nodes}
    f_score[start] = heuristic(start, goal)
    
    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = reconstruct_path(came_from, current)
            return path
        for neighbor, cost in graph.edges[current]:
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None

def heuristic(node, goal):
    # This is a sample heuristic function.
    # You can replace it with a more appropriate heuristic for your specific problem.
    return 0

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

# Example usage:
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_edge("A", "B", 1)
graph.add_edge("B", "C", 3)
graph.add_edge("C", "D", 1)
graph.add_edge("A", "D", 5)

start_node = "A"
goal_node = "C"
result = astar(graph, start_node, goal_node)

if result:
    print(f"Shortest path from {start_node} to {goal_node}: {result}")
else:
    print(f"No path found from {start_node} to {goal_node}")
