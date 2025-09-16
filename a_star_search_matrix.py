import heapq

def astar_search(matrix, start, goal):
    rows, cols = len(matrix), len(matrix[0])

    def heuristic(a, b):
        """Calculate Manhattan distance as the heuristic."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(node):
        """Return valid neighbors of the current node."""
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        for dr, dc in directions:
            r, c = node[0] + dr, node[1] + dc
            if 0 <= r < rows and 0 <= c < cols and matrix[r][c] == 0:
                yield (r, c)

    open_set = []  # Priority queue
    heapq.heappush(open_set, (0, start))  # (priority, node)

    came_from = {}  # To reconstruct the path
    g_score = {start: 0}  # Cost from start to current node
    f_score = {start: heuristic(start, goal)}  # Estimated cost from start to goal

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Return reversed path

        for neighbor in neighbors(current):
            tentative_g_score = g_score[current] + 1  # Cost of 1 for each move

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No path exists

# Example matrix (1s are obstacles, 0s are traversable paths)
matrix = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Starting point
goal = (4, 4)  # Goal point

path = astar_search(matrix, start, goal)
if path:
    print("Path exists from start to goal.")
    print("Shortest Path:", path)
else:
    print("No path exists from start to goal.")
