# Implementing and testing the Binary Search Tree (BST) Insertion and Search
# A Binary Search Tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.
# For each node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """
    Insert a key into a binary search tree rooted at "root".
    """
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    """
    Search for a key in a binary search tree rooted at "root".
    """
    if root is None:
        return False
    if root.val == key:
        return True
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# Pytest for BST insertion and search
def test_bst():
    root = None
    root = insert(root, 5)
    root = insert(root, 3)
    root = insert(root, 8)
    root = insert(root, 2)
    root = insert(root, 4)
    
    assert search(root, 5) == True
    assert search(root, 3) == True
    assert search(root, 8) == True
    assert search(root, 2) == True
    assert search(root, 4) == True
    assert search(root, 6) == False
    assert search(root, 0) == False

# Run the test
test_bst()
print("All BST tests passed!")
