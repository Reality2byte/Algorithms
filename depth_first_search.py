# Depth-First Search (DFS) Algorithm Implementation for Graph
def dfs(graph, start, visited=None):
    """
    Performs Depth-First Search on a graph.
    :param graph: Graph represented as an adjacency list
    :param start: Starting node for the search
    :param visited: Set containing nodes that have been visited
    :return: List of nodes visited in DFS order
    """
    if visited is None:
        visited = set()
    visited.add(start)
    neighbors = graph.get(start, [])
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# Pytest test cases for Depth-First Search (DFS)
def test_dfs():
    graph = {'A': ['B', 'C', 'E'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B'],
             'E': ['A', 'B', 'D'],
             'F': ['C'],
             'G': ['C']}
    assert dfs(graph, 'A') == {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    assert dfs(graph, 'B') == {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    assert dfs(graph, 'C') == {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
    assert dfs({}, 'A') == {'A'}
    assert dfs(graph, 'Z') == {'Z'}

# Running the tests
test_dfs()

