def find_path(maze, start, goal):
    def dfs(current, path):
        if current == goal:
            return path + [current]
        
        x, y = current
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if (0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]) and 
                maze[next_x][next_y] == 0 and (next_x, next_y) not in path):
                result = dfs((next_x, next_y), path + [current])
                if result:
                    return result
        return None

    return dfs(start, [])

# Example maze (0 represents an empty cell, 1 represents an obstacle)
maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0]
]
start = (0, 0)
goal = (3, 3)

path = find_path(maze, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found")
