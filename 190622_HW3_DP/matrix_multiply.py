from typing import List


def get_matrix_chain_recursive(l):
    int_max = [99999999]

    if len(l) < 3:
        return -1
    if len(l) == 3:
        return l[0] * l[1] * l[2]
    helper(l, 0, int_max)
    return int_max[0]


def helper(l, current_result, global_min):
    if current_result >= global_min[0]:
        return
    if len(l) == 3:
        current_result += l[0] * l[1] * l[2]
        if current_result < global_min[0]:
            global_min[0] = current_result
        return
    for i in range(1, len(l) - 1):
        c = l[i] * l[i-1] * l[i+1]
        temp_l = l[:i] + l[i+1:]
        helper(temp_l, current_result + c, global_min)


def get_matrix_chain_dp(p):
    if len(p) < 3:
        return -1
    if len(p) == 3:
        return p[0] * p[1] * p[2]
    l = len(p) - 1

    dp = [[0 for _ in range(l)] for _ in range(l)]

    for r in range(2, l + 1):
        for i in range(l - r + 1):
            j = i + r - 1
            dp[i][j] = dp[i+1][j] + p[i] * p[i+1] * p[j+1]
            for k in range(i+1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + p[i] * p[j+1] * p[k+1])
    return dp[0][l-1]



if __name__ == '__main__':
    print(get_matrix_chain_dp([40, 20, 30, 10, 30]))