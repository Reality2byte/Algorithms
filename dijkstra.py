import heapq
import pytest

def dijkstra(graph, start):
    """
    Dijkstra's algorithm to find the shortest path from a starting node to all other nodes in the graph.
    
    Parameters:
    graph (dict): A dictionary representing the weighted graph.
    start (str): The starting node.
    
    Returns:
    dict: A dictionary containing the shortest distance from the start node to all other nodes.
    """
    # Initialize distances dictionary with infinite distances for all nodes except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to keep track of nodes to be processed
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the current distance is greater than the calculated smallest distance, skip it
        if current_distance > distances[current_node]:
            continue
        
        # Update distances for all neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If the calculated distance is less than the currently known distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# Pytest test cases
def test_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    assert dijkstra(graph, 'A') == {'A': 0, 'B': 1, 'C': 3, 'D': 4}
    assert dijkstra(graph, 'B') == {'A': 1, 'B': 0, 'C': 2, 'D': 3}
    assert dijkstra(graph, 'C') == {'A': 3, 'B': 2, 'C': 0, 'D': 1}
    assert dijkstra(graph, 'D') == {'A': 4, 'B': 3, 'C': 1, 'D': 0}

# Run the test
test_dijkstra()
print("Dijkstra's algorithm test passed.")
