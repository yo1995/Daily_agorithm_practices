from typing import List


def formPolygon(sticks, sides):
    if sides > len(sticks):
        return False
    total_length = sum(sticks)
    side_length = total_length / sides
    # remainder is not zero
    if side_length * sides != total_length:
        return False

    recursive_sticks = []
    for i in range(0, len(sticks)):
        if sticks[i] > side_length:
            return False
        elif sticks[i] < side_length:
            recursive_sticks.append(sticks[i])
        else:
            sides -= 1
    if len(recursive_sticks) == 0:
        return True

    # all remaining sides are shorter than average
    helper(sides, recursive_sticks, side_length)
    if len(recursive_sticks) == 0:
        return True
    return False


def helper(remaining_sides, remaining_sticks, side_length):
    while remaining_sides > 0:
        temp_result = []
        p1(remaining_sticks, side_length, 0, temp_result)
        if not temp_result:  # result not found, remaining sticks are too short to form a side
            return
        else:  # result found
            remaining_sides -= 1
            for s in temp_result:
                remaining_sticks.remove(s)
            continue


def p1(objects, target, cur, result_list):
    if target == 0:
        return True
    if target < 0 or cur >= len(objects):
        return False
    # pick
    result_list.append(objects[cur])
    if p1(objects, target - objects[cur], cur + 1, result_list):
        return result_list
    # no pick
    result_list.pop(len(result_list) - 1)
    if p1(objects, target, cur + 1, result_list):
        return result_list
    return []


if __name__ == '__main__':
    _sticks = [1,2,3,2,1]
    _sides = 4
    res = formPolygon(_sticks, _sides)
    print(res)
