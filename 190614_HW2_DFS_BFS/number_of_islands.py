from collections import deque
from typing import List


class Solution:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        q1 = deque()
        start_set = self.find_start(grid)
        if not start_set:
            return 0
        count = 0
        while start_set:
            sX, sY = start_set.pop()
            q1.append((sX, sY))
            grid[sX][sY] = 'X'
            while q1:
                topX, topY = q1.popleft()
                for i in range(4):
                    x = topX + self.dx[i]
                    y = topY + self.dy[i]
                    if row > x >= 0 <= y < col and grid[x][y] == '1':
                        if (x, y) in start_set:
                            start_set.remove((x, y))
                        if grid[x][y] == 'X':  # already visited
                            continue
                        grid[x][y] = 'X'
                        q1.append((x, y))
            count += 1
        return count

    def num_different_size(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        q1 = deque()
        start_set = self.find_start(grid)
        count = 0
        size_set = set()
        if not start_set:
            return 0
        while start_set:
            sX, sY = start_set.pop()
            q1.append((sX, sY))
            grid[sX][sY] = 'X'
            island_size = 0
            while q1:
                topX, topY = q1.popleft()
                for i in range(4):
                    x = topX + self.dx[i]
                    y = topY + self.dy[i]
                    if row > x >= 0 <= y < col and grid[x][y] == '1':
                        if (x, y) in start_set:
                            start_set.remove((x, y))
                        if grid[x][y] == 'X':
                            continue
                        grid[x][y] = 'X'
                        island_size += 1
                        q1.append((x, y))
            count += 1
            if island_size in size_set:
                count -= 1
            else:
                size_set.add(island_size)
        return count

    def find_start(self, grid):
        start_set = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    start_set.add((i, j))
        return start_set


if __name__ == '__main__':

    # g = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
    g = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    sol = Solution()
    print(sol.num_different_size(g))
