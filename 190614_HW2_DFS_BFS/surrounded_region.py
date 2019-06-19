from typing import List
from collections import deque

maze = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,0,1,1],
]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction_char: [str] = ['D', 'R', 'U', 'L']  # 往小走是 up，往大走是 down


def solve(board: List[List[int]]):
    row = len(board)
    col = len(board[0])
    if row == 0 or col == 0:
        return
    for j in range(col):
        search_BFS(board, 0, j)
        search_BFS(board, row - 1, j)
    for i in range(row):
        search_BFS(board, i, 0)
        search_BFS(board, i, col - 1)
    # recover the board
    for i in range(row):
        for j in range(col):
            if board[i][j] == -1:
                board[i][j] = 0
            else:
                board[i][j] = 1
    for r in board:
        print(r)


def search_BFS(board, x: int, y: int):
    if board[x][y] == 1:
        return
    row = len(board)
    col = len(board[0])
    q1 = deque()
    q1.append((x, y))
    board[x][y] = -1
    while q1:
        topX, topY = q1.popleft()
        for i in range(4):
            topX += dx[i]
            topY += dy[i]
            if row > topX >= 0 <= topY < col and maze[x][y] == 0:
                board[topX][topX] = -1
                q1.append((topX, topY))


def search_DFS(board, x: int, y: int):
    if board[x][y] != 0:
        return
    board[x][y] = -1
    row = len(board)
    col = len(board[0])
    if x > 1:
        search_DFS(board, x-1, y)
    if x < row - 2:
        search_DFS(board, x+1, y)
    if y > 1:
        search_DFS(board, x, y-1)
    if y < col - 2:
        search_DFS(board, x, y+1)


if __name__ == '__main__':
    solve(maze)
