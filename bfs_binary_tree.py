class TreeNode:
    def __init__(self, value, left=None, right=None):
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

def bfs(root):
    if not root:
        return []

    visited_nodes = []  # To store the order of visited nodes
    queue = [root]      # Queue for BFS (FIFO)

    while queue:
        node = queue.pop(0)  # Remove the front element of the queue
        visited_nodes.append(node.value)  # Process the current node

        # Add children of the current node to the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited_nodes

# Call BFS and print the result
visited_nodes = bfs(root)
print(visited_nodes)
  