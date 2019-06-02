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
        if num[pos] == '0' and i != pos:  # the first char is 0, and we did not do + 0 + operation, thus invalid
            break
            pass
        current_num_str = num[pos: i+1]
        current_num = int(current_num_str)
        if pos == 0:  # the first number in result list is added into it with no operator.
            helper(num, target, temp + current_num_str, i + 1, current_num, current_num, result)
        else:
            helper(num, target, temp + '+' + current_num_str, i + 1, current + current_num, current_num, result)
            helper(num, target, temp + '-' + current_num_str, i + 1, current - current_num, - current_num, result)
            helper(num, target, temp + '*' + current_num_str, i + 1, current - last + current_num * last, current_num * last, result)
            if current_num != 0 and last % current_num == 0:  # remainder is zero
                helper(num, target, temp + '/' + current_num_str, i + 1, current - last + last / current_num,
                            last / current_num, result)
    return


if __name__ == '__main__':
    number = '10523'
    results = luckyNumbers(number, 7)
    print(results, len(results))
