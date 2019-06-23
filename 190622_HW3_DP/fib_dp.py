from typing import List


def fib_dp(start) -> int:
    if start <= 1:
        return 1
    result = [0 for _ in range(start)]
    result[0] = 1
    result[1] = 1
    for i in range(2, start):
        result[i] = result[i-1] + result[i-2]
    return result[start-1]


if __name__ == '__main__':
    print(fib_dp(7))
