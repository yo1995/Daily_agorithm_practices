from typing import List


def combine_ropes(ropes: List[List[str]]) -> bool:
    count = 0
    prev = len(ropes)
    ropes_remaining = ropes
    while ropes_remaining:
        print(ropes_remaining)
        if count == prev:
            return False
        current_rope = [ropes_remaining[0][0], ropes_remaining[0][1]]
        prev = len(ropes)
        count = 1
        temp = []
        for rope in ropes_remaining[1:]:
            if rope[0] == current_rope[0]:
                current_rope = [rope[1], current_rope[1]]
            elif rope[0] == current_rope[1]:
                current_rope = [current_rope[0], rope[1]]
            elif rope[1] == current_rope[0]:
                current_rope = [rope[0], current_rope[1]]
            elif rope[1] == current_rope[1]:
                current_rope = [current_rope[0], rope[0]]
            else:
                count += 1
                temp.append(rope)
                continue
        if not temp:
            return True
        else:
            temp.append(current_rope)
            ropes_remaining = temp
    return True


if __name__ == '__main__':
    test1 = [['a', 'b'], ['c', 'd'], ['e', 'f'], ['f', 'g'], ['c', 'g'], ['b', 'd']]
    test2 = [['a', 'a'], ['b', 'b'], ['c', 'd']]
    test3 = [['a', 'a']]
    test4 = [['a', 'a'], ['a', 'b'], ['b', 'c']]
    print(combine_ropes(test2))
