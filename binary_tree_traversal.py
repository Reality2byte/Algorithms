# Implementing the Binary Tree Traversal Algorithms
# We will implement in-order, pre-order, and post-order tree traversal algorithms.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# In-order traversal
def inorder_traversal(root: TreeNode) -> List[int]:
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

# Pre-order traversal
def preorder_traversal(root: TreeNode) -> List[int]:
    if root is None:
        return []
    return [root.value] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Post-order traversal
def postorder_traversal(root: TreeNode) -> List[int]:
    if root is None:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.value]

# Pytest test cases for tree traversal algorithms

def test_tree_traversal():
    # Creating a sample tree: 
    #         1
    #        / \
    #       2   3
    #      / \ / \
    #     4  5 6  7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    assert inorder_traversal(root) == [4, 2, 5, 1, 6, 3, 7]
    assert preorder_traversal(root) == [1, 2, 4, 5, 3, 6, 7]
    assert postorder_traversal(root) == [4
