from typing import List

def fib_dp(start) -> int:
    if start <= 1:
        return 1
    result = [0 for i in range(start + 1)]
    