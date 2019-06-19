from typing import List
from collections import deque


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction_char: [str] = ['D', 'R', 'U', 'L']  # 往小走是 up，往大走是 down

maze = [
    [0,0,0,0,0],
    [1,1,0,0,1],
    [0,0,0,0,0],
    [0,1,0,0,1],
    [0,1,0,0,0]
]

inf = 99999


def find_shortest_path(maze: List[List[int]], startX: int, startY: int, targetX: int, targetY: int) -> (int, List[str]):
    row = len(maze)
    col = len(maze[0])
    distance_mat = [[inf for _ in range(col)] for _ in range(row)]
    q1 = deque()
    q1.append((startX, startY))
    distance_mat[startX][startY] = 0
    path_mat = [['' for _ in range(col)] for _ in range(row)]
    while q1:
        topX, topY= q1.popleft()
        for i in range(4):
            x = topX
            y = topY
            d = distance_mat[x][y]
            path = path_mat[x][y]
            while row > x >= 0 <= y < col and maze[x][y] == 0 and (x != targetX or y != targetY):
                x += dx[i]
                y += dy[i]
                d += 1
            if x != targetX or y != targetY:
                x -= dx[i]
                y -= dy[i]
                d -= 1
            new_path = path + direction_char[i]
            if distance_mat[x][y] > d or (distance_mat[x][y] == d and path_mat[x][y] > new_path):
                distance_mat[x][y] = d
                path_mat[x][y] = new_path
                if x != targetX or y != targetY:
                    q1.append((x, y))

    result = path_mat[targetX][targetY]
    if distance_mat[targetX][targetY] == inf:
        return 'impossible'
    print(path_mat)
    return result


if __name__ == '__main__':
    print(find_shortest_path(maze, 4, 3, 0, 1))
