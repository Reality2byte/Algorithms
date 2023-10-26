# Corrected A* pathfinding algorithm

def a_star(graph, start, goal):
    """
    A* pathfinding algorithm to find the shortest path from start to goal in a graph.

    Parameters:
    - graph: a dictionary where keys are nodes and values are dictionaries of neighbors and their costs
    - start: the starting node
    - goal: the goal node

    Returns:
    - path: a list of nodes from start to goal, or None if no path exists
    """
    # Priority queue to store (cost, current_node, path_so_far)
    frontier = [(0, start, [start])]
    # Set to store explored nodes
    explored = set()

    while frontier:
        # Get the node in the frontier with the least cost
        cost, current, path = heapq.heappop(frontier)

        # If this node is the goal, return the path to it
        if current == goal:
            return path

        # Mark the current node as explored
        if current in explored:
            continue
        explored.add(current)

        # Go through all neighbors of the current node
        for neighbor, neighbor_cost in graph[current].items():
            new_cost = cost + neighbor_cost

            # Add neighbor to the frontier
            if neighbor not in explored:
                heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))

# Rerun the test cases for the corrected A* algorithm

def test_a_star():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    assert a_star(graph, 'A', 'D') == ['A', 'B', 'C', 'D']
    assert a_star(graph, 'A', 'C') == ['A', 'B', 'C']
    assert a_star(graph, 'A', 'A') == ['A']
    assert a_star(graph, 'A', 'Z') == None

test_a_star()
print("A* algorithm test passed")
