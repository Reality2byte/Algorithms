# Now let's implement the Floyd-Warshall algorithm, which is used for finding shortest paths in a weighted graph.
# This algorithm works for both directed and undirected graphs and also handles negative weight edges.

def floyd_warshall(graph):
    """
    Find the shortest paths between all pairs of nodes using the Floyd-Warshall algorithm.
    
    Parameters:
    graph (dict): A dictionary representing the weighted graph.
                  Keys are nodes, and values are lists of (neighbor, weight) tuples.
    
    Returns:
    dict: A dictionary where keys are source nodes and values are dictionaries mapping target nodes to shortest path lengths.
    """
    # Initialize distance dictionary
    dist = {}
    for node in graph:
        dist[node] = {}
        for neighbor in graph:
            if node == neighbor:
                dist[node][neighbor] = 0
            else:
                dist[node][neighbor] = float('inf')
    
    # Update distances from the graph
    for node in graph:
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight
    
    # Floyd-Warshall algorithm
    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Test the Floyd-Warshall algorithm implementation
def test_floyd_warshall():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    dist = floyd_warshall(graph)
    assert dist['A']['A'] == 0
    assert dist['A']['B'] == 1
    assert dist['A']['C'] == 3
    assert dist['A']['D'] == 4
    assert dist['B']['D'] == 3

# Run the test and print the output
test_floyd_warshall()
"Floyd-Warshall algorithm test passed!"
