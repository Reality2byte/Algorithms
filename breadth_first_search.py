from collections import deque

# Breadth-First Search (BFS) Algorithm Implementation for Graph
def bfs(graph, start):
    """
    Performs Breadth-First Search on a graph.
    :param graph: Graph represented as an adjacency list
    :param start: Starting node for the search
    :return: List of nodes visited in BFS order
    """
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            neighbors = graph.get(vertex, [])
            queue.extend(neighbors)
    return visited

# Pytest test cases for Breadth-First Search (BFS)
def test_bfs():
    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}
    assert bfs(graph, 'A') == {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    assert bfs(graph, 'B') == {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    assert bfs(graph, 'C') == {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    assert bfs({}, 'A') == {'A'}
    assert bfs(graph, 'Z') == {'Z'}

# Running the tests
test_bfs()

