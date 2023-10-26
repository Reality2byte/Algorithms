# Next, let's implement the Bellman-Ford algorithm for finding the shortest path in a weighted graph.
# Unlike Dijkstra's algorithm, Bellman-Ford can handle graphs with negative weight edges.

def bellman_ford(graph, start):
    """
    Find the shortest paths from a start node to all other nodes using the Bellman-Ford algorithm.
    
    Parameters:
    graph (dict): A dictionary representing the weighted graph.
                  Keys are nodes, and values are lists of (neighbor, weight) tuples.
    start (str): The start node.
    
    Returns:
    dict: A dictionary mapping each node to its shortest path length from the start node.
    """
    # Initialize distance dictionary
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    
    # Bellman-Ford algorithm
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
    
    # Check for negative weight cycles
    for node in graph:
        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")
    
    return dist

# Test the Bellman-Ford algorithm implementation
def test_bellman_ford():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    dist = bellman_ford(graph, 'A')
    assert dist['A'] == 0
    assert dist['B'] == 1
    assert dist['C'] == 3
    assert dist['D'] == 4

# Run the test and print the output
test_bellman_ford()
