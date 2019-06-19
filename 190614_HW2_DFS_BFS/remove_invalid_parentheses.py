from typing import List
from collections import deque


def is_valid(s: str) -> bool:
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


def remove_invalid_parentheses(s: str) -> List[str]:
    result = []  # multiple string might be in the results
    q1 = deque()
    checked = set()
    found = False
    max_count = 0
    q1.append(s)
    while q1:
        top = q1.popleft()
        if is_valid(top):
            found = True
            if len(top) >= max_count and top not in result:
                result.append(top)
                max_count = len(top)
        if found:
            continue
        for i in range(len(top)):
            prev = top[:i]
            next = top[i+1:]
            temp_str = prev + next
            if temp_str not in checked:
                q1.append(temp_str)
                checked.add(temp_str)
    if not found:
        return ['']
    return result


if __name__ == '__main__':
    # p = '()())()'
    p = ')(f'
    print(remove_invalid_parentheses(p))
