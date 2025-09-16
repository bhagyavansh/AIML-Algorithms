import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g  # Cost from start to the current node
        self.h = h  # Heuristic cost to the goal
        self.f = g + h  # Total cost

    def __eq__(self, other):
        return self.position == other.position


        

    def __lt__(self, other):
        return self.f < other.f

    def update_costs(self, g, h):
        self.g = g
        self.h = h
        self.f = g + h

def heuristic(a, b):
    """Calculate the Manhattan distance as the heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(node, matrix):
    """Get valid neighbors of the current node."""
    neighbors = []
    rows, cols = len(matrix), len(matrix[0])
    row, col = node.position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] == 0:
            neighbors.append((new_row, new_col))
    return neighbors

def a_star(matrix, start, end):
    """Perform A* search to find the shortest path."""
    start_node = Node(start, None, 0, heuristic(start, end))
    end_node = Node(end, None)
    open_list = []
    heapq.heappush(open_list, start_node)
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        # Check if the goal is reached
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get start-to-end order

        closed_list.add(current_node.position)

        # Explore neighbors
        for neighbor_pos in get_neighbors(current_node, matrix):
            if neighbor_pos in closed_list:
                continue

            neighbor_g = current_node.g + 1  # Increment cost by 1 for each step
            neighbor_node = Node(neighbor_pos, current_node, neighbor_g, heuristic(neighbor_pos, end))

            # Skip nodes already in the open list with a lower or equal cost
            if any(open_node.position == neighbor_node.position and open_node.f <= neighbor_node.f for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Example usage
matrix = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)
path = a_star(matrix, start, end)

if path:
    print("Shortest Path:", path)
else:
    print("No path found")
