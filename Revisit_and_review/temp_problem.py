from typing import List


def luckyNumbers(nums, target):
    result = []
    helper(nums, target, "", 0, 0, 0, result)
    return result


def helper(num, target, temp, pos, current, last, result):
    """

    :param num: the input digits string
    :param target: the number to find
    :param temp: temp result string
    :param pos: current pointer position to the input string
    :param current: calculated result
    :param last: use to calculate * and / that need to change order
    :param result: the result list to store all valid result strings
    :return: None
    """
    if pos == len(num):
        if current == target:
            result.append(temp)
            pass
        return
    for i in range(pos, len(num)):
        if num[pos] == '0' and i != pos:
            break
        m = num[pos:i+1]
        n = int(m)
        if pos == 0:
            helper(num, target, temp + m, i + 1, current + n, n, result)
            pass
        else:
            helper(num, target, temp + '+' + m, i + 1, current + n, n, result)
            helper(num, target, temp + '-' + m, i + 1, current - n, -n, result)
            helper(num, target, temp + '*' + m, i + 1, current - last + last * n, last * n, result)
            if n != 0 and last % n == 0:
                helper(num, target, temp + '/' + m, i + 1, int(current - last + last / n), int(last / n), result)
                pass
            pass
    return


if __name__ == '__main__':
    number = '123456'
    results = luckyNumbers(number, 1)
    print(results, len(results))
