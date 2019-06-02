from typing import List


def knapsack_no_value(target: int, objects: List[int], cur: int) -> bool:
    """
    we should assume objects are in heavy to light order

    :param target: the target weight, or the capacity of the knapsack
    :param objects: all available weights for items
    :param cur: current index in objects
    :return: exact fit or not
    """
    if target == 0:
        # either meet the weight or no weight at all
        return True
    if target < 0 or cur >= len(objects):
        # too heavy item or no more items fit
        return False
    # no pick or pick current item
    return knapsack_no_value(target, objects, cur + 1) or knapsack_no_value(target - objects[cur], objects, cur + 1)


if __name__ == '__main__':
    items = [2, 5, 10, 20, 50, 100]
    items.reverse()
    print(knapsack_no_value(23, items, 0))
