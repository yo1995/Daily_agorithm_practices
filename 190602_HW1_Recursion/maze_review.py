from typing import List

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction_char: [str] = ['R', 'U', 'L', 'D']


def solve_maze_recursion(maze: List[List[int]], startX: int, startY: int, targetX: int, targetY: int, path: List[str]) -> bool:
    if startX < 0 or startY < 0 or startY > len(maze) or startX > len(maze[0]):
        return False
    if startX == targetX and startY == targetY:
        return True
    maze[start[0]][start[1]] = 1  # mark as visited
    for i in range(0, 4):
        path.append(direction_char[i])
        if solve_maze_recursion(maze, startX + dx[i], startY + dy[i], targetX, targetY, path):
            return True
        path.pop(len(path) - 1)
    return false
