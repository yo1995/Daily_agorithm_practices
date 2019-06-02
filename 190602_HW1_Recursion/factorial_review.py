import typing


def factorial_tail_recursion(n: int, total: int) -> int:
    if n == 1:
        return total
    return factorial_tail_recursion(n - 1, n * total)


def factorial_iteration(n: int) -> int:
    total: int = 1
    while n > 1:
        total *= n
        n -= 1
        pass
    return total


if __name__ == '__main__':
    print(factorial_tail_recursion(5, 1))
    print(factorial_iteration(5))
