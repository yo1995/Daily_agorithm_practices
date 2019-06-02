from typing import List

def subsetSums(elements, K):
    """

    :param elements: possible weights
    :param K: target
    :return: a list of result lists
    """
    results = []
    new_elements = []
    for e in elements:
        if e <= K:
            new_elements.append(e)
    helper(new_elements, K, 0, [], results)
    return results


def helper(objects, target, cur, result_list, all_results):
    if target == 0:
        all_results.append(result_list.copy())
        return
    if target < 0 or cur >= len(objects):
        return
    # pick
    result_list.append(objects[cur])
    helper(objects, target - objects[cur], cur + 1, result_list, all_results)
    # no pick
    result_list.pop(len(result_list) - 1)
    helper(objects, target, cur + 1, result_list, all_results)
    return


if __name__ == '__main__':
    _elements = [1,2,3,4,5,6]
    _K = 5
    res = subsetSums(_elements, _K)
    a = res.__str__()
    b = ''
    for i in a:
        if i != ' ':
            b += i
    print(b)
