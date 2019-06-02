from typing import List


def gray_code(n: int) -> List[int]:
    result: List[int] = []
    helper(n, result)
    return result


def helper(n: int, result: List[int]):
    if n == 0:
        result.append(0)
        return
    helper(n-1, result)
    k = 1 << (n-1)
    for i in range(len(result) - 1, -1, -1):
        result.append(result[i] + k)
        pass


if __name__ == '__main__':
    print([bin(i) for i in gray_code(3)])
