from typing import List


def calculate_health(dungeon: List[List[int]]):
    int_max = 10000
    l1 = len(dungeon)
    l2 = len(dungeon[0])
    dp = [[int_max for _ in range(l2 + 1)] for _ in range(l1 + 1)]

    # can also only set 2 values to reduce time cost
    for i in range(len(dungeon[0]) + 1):
        dp[l1][l2 - 1] = 1
    for j in range(len(dungeon) + 1):
        dp[l1 - 1][l2] = 1

    for i in range(l1, 0, -1):
        for j in range(l2, 0, -1):
            req = min(dp[i][j-1], dp[i-1][j]) - dungeon[i-1][j-1]
            if req <= 0:
                dp[i-1][j-1] = 1
            else:
                dp[i-1][j-1] = req

    return dp[0][0]


if __name__ == '__main__':
    d = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    print(calculate_health(d))
