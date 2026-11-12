from collections import deque


# ==========================================
# GRAPH IMPLEMENTATION
# ==========================================
class UndirectedGraph:
    def __init__(self):
        self.adjacency_list: dict[str, list[str]] = {}

    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1: str, v2: str) -> None:
        self.add_vertex(v1)
        self.add_vertex(v2)
        if v2 not in self.adjacency_list[v1]:
            self.adjacency_list[v1].append(v2)
        if v1 not in self.adjacency_list[v2]:
            self.adjacency_list[v2].append(v1)

    def bfs(self, start_vertex: str) -> list[str]:
        """Breadth-First Search (BFS) Traversal for Graph."""
        visited_set = {start_vertex}
        queue = deque([start_vertex])
        traversal_order = []

        while queue:
            current = queue.popleft()
            traversal_order.append(current)

            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in visited_set:
                    visited_set.add(neighbor)
                    queue.append(neighbor)

        return traversal_order

    def dfs(self, start_vertex: str) -> list[str]:
        """Depth-First Search (DFS) Traversal for Graph."""
        visited_set = set()
        stack = [start_vertex]
        traversal_order = []

        while stack:
            current = stack.pop()
            if current not in visited_set:
                visited_set.add(current)
                traversal_order.append(current)

                # Reverse neighbors so leftmost neighbor is popped first
                for neighbor in reversed(self.adjacency_list.get(current, [])):
                    if neighbor not in visited_set:
                        stack.append(neighbor)

        return traversal_order


def build_sellote_graph() -> UndirectedGraph:
    """
    Constructs an Undirected Graph using the letters of 'SELLOTE':
    Vertices: S, E1, L1, L2, O, T, E2
    """
    graph = UndirectedGraph()

    edges = [
        ("S", "E1"), ("S", "L1"), ("S", "L2"),
        ("E1", "L1"), ("E1", "O"),
        ("L1", "L2"), ("L1", "O"), ("L1", "T"),
        ("L2", "T"), ("L2", "E2")
    ]

    for v1, v2 in edges:
        graph.add_edge(v1, v2)

    return graph


# ==========================================
# MAIN EXECUTION
# ==========================================
if __name__ == "__main__":
    print("=== ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE (SELLOTE) ===\n")

    sellote_graph = build_sellote_graph()
    print("===========================================================")
    print("GRAPH ('S', 'E1', 'L1', 'L2', 'O', 'T', 'E2')")
    print("===========================================================\n")
    print("   BFS Traversal :", " -> ".join(sellote_graph.bfs("S")))
    print("   DFS Traversal :", " -> ".join(sellote_graph.dfs("S")))