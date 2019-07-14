
def is_overlap(arr1, arr2):
    if arr2[0] <= arr1[0] <= arr2[1]:
        return True
    if arr2[0] <= arr1[1] <= arr2[1]:
        return True
    if arr1[0] <= arr2[0] <= arr1[1]:
        return True
    if arr1[0] <= arr2[1] <= arr1[1]:
        return True
    return False


def merge_2_arrays(arr1, arr2):
    l = min(min(arr1), min(arr2))
    r = max(max(arr1), max(arr2))
    return [l, r]


def rain_drop(rain):
    if not rain:
        return -1
    r = sorted(rain)
    covered = r[0]
    for i in range(1, len(r)):

        if not is_overlap(covered, r[i]):
            return -1
        covered = merge_2_arrays(covered, r[i])
        print(covered)
        if covered[1] >= 1:
            return i + 1
    return -1


if __name__ == '__main__':
    rains = [[0, 0.3],[0.3, 0.6],[0.5, 0.8], [0.67, 1], [0, 0.4] ,[0.5, 0.75]]
    print(rain_drop(rains))