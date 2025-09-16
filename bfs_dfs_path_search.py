from collections import deque

# Define a tree node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Construct the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# BFS function
def bfs(root, x):
    if not root:
        return []

    queue = deque([(root, [root.value])])  # Queue stores (node, path to the node)
    while queue:
        node, path = queue.popleft()

        if node.value == x:  # Agar x mil gaya, toh return path
            return path

        if node.left:  # Agar left child hai toh add karo queue mein
            queue.append((node.left, path + [node.left.value]))
        if node.right:  # Agar right child hai toh add karo queue mein
            queue.append((node.right, path + [node.right.value]))

    return []  # Agar element nahi mila toh empty list return karo

# DFS function
def dfs(root, x):
    if not root:
        return []

    stack = [(root, [root.value])]  # Stack stores (node, path to the node)
    while stack:
        node, path = stack.pop()  # Stack se last element nikalte hain (LIFO)

        if node.value == x:  # Agar x mil gaya, toh return path
            return path

        if node.right:  # Right child ko pehle stack mein add karte hain
            stack.append((node.right, path + [node.right.value]))
        if node.left:  # Fir left child ko add karte hain
            stack.append((node.left, path + [node.left.value]))

    return []  # Agar element nahi mila toh empty list return karo

# User input for choice and element to search
k = int(input("Choose 1 for BFS or 2 for DFS: "))
x = int(input("Enter the element to search for: "))

if k == 1:
    path = bfs(root, x)
elif k == 2:
    path = dfs(root, x)
else:
    print("Invalid choice.")
    path = []

# Print the result
if path:
    print("Path is:", path)
else:
    print("Path is not found.")
