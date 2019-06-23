from typing import List


def LCS(s1: str, s2: str) -> List[List[int]]:
    l1 = len(s1)
    l2 = len(s2)
    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # for r in dp:
    #     print(r)
    return dp


def super_sequence(s1: str, s2: str) -> str:
    l1 = len(s1)
    l2 = len(s2)

    dp = LCS(s1, s2)

    result = ''
    while l1 > 0 or l2 > 0:
        if l1 == 0:
            result = s2[:l2] + result
            break
        if l2 == 0:
            result = s1[:l1] + result
            break

        if s1[l1-1] == s2[l2-1]:
            result = s1[l1-1] + result
            l1 -= 1
            l2 -= 1
            continue

        if dp[l1][l2] == dp[l1-1][l2]:
            result = s1[l1-1] + result
            l1 -= 1
        else:
            result = s2[l2-1] + result
            l2 -= 1
    return result


if __name__ == '__main__':
    print(super_sequence('abac', 'cab'))  # 'AGGTAB', 'GXTXAYB' -> AGXGTXAYB
