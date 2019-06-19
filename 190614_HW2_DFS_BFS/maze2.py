from typing import List
from collections import deque
import math


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction_char: [str] = ['R', 'U', 'L', 'D']


maze = [
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0]
]

inf = 99999


def find_shortest_path(maze: List[List[int]], startX: int, startY: int, targetX: int, targetY: int) -> int:
    row = len(maze)
    col = len(maze[0])
    distance_mat = [[inf for _ in range(col)] for _ in range(row)]
    q1 = deque()
    q1.append((startX, startY))
    distance_mat[startX][startY] = 0
    while q1:
        topX, topY = q1.popleft()

        for i in range(4):
            x = topX
            y = topY
            d = distance_mat[x][y]
            while row > x >= 0 <= y < col and maze[x][y] == 0:
                x += dx[i]
                y += dy[i]
                d += 1
            # back one step
            x -= dx[i]
            y -= dy[i]
            d -= 1
            if distance_mat[x][y] > d:
                distance_mat[x][y] = d
                if x != targetX or y != targetY:
                    q1.append((x, y))

    res = distance_mat[targetX][targetY]
    if res == inf:
        return -1
    return res


if __name__ == '__main__':
    print(find_shortest_path(maze, 0, 4, 4, 4))
