# Let's start by implementing the Prim's algorithm for finding the minimum spanning tree of a weighted graph.
# Prim's algorithm starts with an arbitrary node and grows the minimum spanning tree one vertex at a time by adding
# the cheapest edge from the tree to another vertex.

from heapq import heappop, heappush
import pytest

def prims_algorithm(graph):
    """
    Find the minimum spanning tree using Prim's algorithm.
    
    Parameters:
    graph (dict): A dictionary representing the weighted graph.
                  Keys are nodes, and values are lists of (neighbor, weight) tuples.
    
    Returns:
    list: A list of edges forming the minimum spanning tree.
    """
    # Initialize the minimum spanning tree and priority queue
    mst = []
    pq = [(0, None, list(graph.keys())[0])]
    
    # Keep track of visited nodes
    visited = set()
    
    while pq:
        cost, parent, node = heappop(pq)
        
        # Skip if the node is already visited
        if node in visited:
            continue
        
        visited.add(node)
        
        # Add edge to MST if it's not the initial node
        if parent is not None:
            mst.append((parent, node, cost))
        
        # Add neighbors to the priority queue
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heappush(pq, (weight, node, neighbor))
    
    return mst

# Test the Prim's algorithm implementation
def test_prims_algorithm():
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    mst = prims_algorithm(graph)
    expected_mst = [('A', 'B', 1), ('B', 'C', 2), ('C', 'D', 1)]
    
    # Sort the edges to make comparison easier
    mst = sorted(mst)
    expected_mst = sorted(expected_mst)
    
    assert mst == expected_mst

# Run the test and print the output
test_prims_algorithm()
"Prim's algorithm test passed!"
