# Let's move on to implementing the next algorithm: Kruskal's algorithm.
# Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.

# We'll start by defining helper functions to handle disjoint-set (Union-Find) data structure.

def make_set(x):
    """Create a singleton set containing element x."""
    return {x: {'parent': x, 'rank': 0}}

def find_set(sets, x):
    """Find the representative of the set containing x."""
    if sets[x]['parent'] != x:
        sets[x]['parent'] = find_set(sets, sets[x]['parent'])
    return sets[x]['parent']

def union(sets, x, y):
    """Merge the sets containing x and y."""
    x_root = find_set(sets, x)
    y_root = find_set(sets, y)

    if x_root == y_root:
        return

    if sets[x_root]['rank'] < sets[y_root]['rank']:
        sets[x_root]['parent'] = y_root
    elif sets[x_root]['rank'] > sets[y_root]['rank']:
        sets[y_root]['parent'] = x_root
    else:
        sets[y_root]['parent'] = x_root
        sets[x_root]['rank'] += 1

# Now let's implement Kruskal's algorithm

def kruskal(graph):
    """
    Kruskal's algorithm to find a minimum spanning tree of a weighted, undirected graph.

    Parameters:
    - graph: a list of edges, where each edge is a tuple (u, v, w) representing an edge from u to v with weight w

    Returns:
    - A list of edges forming the minimum spanning tree
    """
    # Sort edges by weight
    graph.sort(key=lambda x: x[2])

    mst = []
    sets = {}

    # Initialize disjoint sets for each node
    for u, v, _ in graph:
        if u not in sets:
            sets.update(make_set(u))
        if v not in sets:
            sets.update(make_set(v))

    # Iterate through sorted edges and add them to MST if they don't form a cycle
    for u, v, w in graph:
        if find_set(sets, u) != find_set(sets, v):
            mst.append((u, v, w))
            union(sets, u, v)

    return mst

# Test cases for Kruskal's algorithm

def test_kruskal():
    graph = [
        ('A', 'B', 1),
        ('B', 'C', 2),
        ('A', 'C', 2),
        ('C', 'D', 1),
        ('B', 'D', 2)
    ]
    assert kruskal(graph) == [('A', 'B', 1), ('C', 'D', 1), ('B', 'C', 2)]
    graph = [
        ('A', 'B', 3),
        ('B', 'C', 1),
        ('A', 'C', 4),
        ('C', 'D', 2),
        ('D', 'E', 5)
    ]
    assert kruskal(graph) == [('B', 'C', 1), ('C', 'D', 2), ('A', 'B', 3), ('D', 'E', 5)]

test_kruskal()
print("Kruskal's algorithm test passed")
