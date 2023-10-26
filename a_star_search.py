# Next, let's implement the A* Search algorithm for pathfinding.
# The A* algorithm uses a heuristic to estimate the cost to reach the goal from a given node.
# It operates efficiently compared to other pathfinding algorithms like Dijkstra's algorithm when a good heuristic is used.

from typing import List, Tuple
from heapq import heappop, heappush

def a_star_search(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
    # Initialize the priority queue with the start node and its cost
    pq = [(0, start)]
    
    # Initialize a dictionary to store the cost to reach each node
    g_cost = {start: 0}
    
    # Initialize a dictionary to store the parent of each node
    came_from = {start: None}
    
    # Define the possible movements (up, down, left, right)
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while pq:
        # Get the node with the lowest total cost (f_cost)
        _, current = heappop(pq)
        
        # Check if the goal has been reached
        if current == goal:
            # Reconstruct the path and return it
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        # Explore the neighbors of the current node
        for dx, dy in moves:
            x, y = current
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)
            
            # Check if the neighbor is within the grid and not an obstacle
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                # Calculate the new cost to reach the neighbor
                new_g_cost = g_cost[current] + 1
                
                # Update the cost and parent if this is a better path
                if new_g_cost < g_cost.get(neighbor, float('inf')):
                    g_cost[neighbor] = new_g_cost
                    # Estimate the cost to reach the goal from the neighbor (using Manhattan distance)
                    h_cost = abs(goal[0] - nx) + abs(goal[1] - ny)
                    f_cost = new_g_cost + h_cost
                    heappush(pq, (f_cost, neighbor))
                    came_from[neighbor] = current
                    
    return []  # Return an empty list if no path is found

# Test the a_star_search function
def test_a_star_search():
    grid = [
        [0, 0, 0, 
