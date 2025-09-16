class TreeNode:
    def __init__(self, value=0, left=None, right=None):  # Fixed syntax: `def__init__` to `def __init__`
        self.value = value
        self.left = left
        self.right = right

# Construct the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Check if the tree is constructed
if not root:
    print("Not constructed")
else:
    print("Properly constructed")

# Define DFS function
def dfs(root):
    if not root:
        return []

    visited_nodes = []  # To store the visited nodes
    stack = [root]      # Stack for DFS (LIFO)

    while stack:
        node = stack.pop()  # Pop the top element from the stack
        visited_nodes.append(node.value)  # Process the current node

        # Push right child first so the left child is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited_nodes

# Call DFS and print the result
visited_nodes = dfs(root)
print(visited_nodes)
