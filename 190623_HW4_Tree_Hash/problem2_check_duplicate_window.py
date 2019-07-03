


def check_duplicate(array, k):
    s = set(array[:k])
    if len(s) < k:
        return True
    l = len(array)
    if l < k:
        return False
    for i in range(k, l):
        top = array[i-k]
        if array[i] in s:
            return True
        s.remove(top)
        s.add(array[i])
    return False

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 1, 2, 3, 4]
    k = 3
    print(check_duplicate(arr, k))

