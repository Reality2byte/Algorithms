# Implementing and testing the Topological Sort Algorithm
# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge (u, v), vertex u comes before v in the ordering.

from collections import deque

def topological_sort(graph):
    """
    Perform topological sort on a directed acyclic graph.
    """
    in_degree = {u: 0 for u in graph}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque()
    for u in in_degree:
        if in_degree[u] == 0:
            queue.append(u)
    
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    return result if len(result) == len(graph) else []

# Pytest for the topological_sort function
def test_topological_sort():
    graph1 = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['F'],
        'E': ['H', 'F'],
        'F': ['G'],
        'G': [],
        'H': []
    }
    assert set(topological_sort(graph1)) == set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    
    graph2 = {
        'A': [],
        'B': ['A'],
        'C': ['A'],
        'D': ['B', 'C']
    }
    assert set(topological_sort(graph2)) == set(['A', 'B', 'C', 'D'])

# Run the test
test_topological_sort()
print("All topological_sort tests passed!")
