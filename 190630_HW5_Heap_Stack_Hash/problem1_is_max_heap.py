from collections import deque


def is_max_heap(array):
    if len(array) <= 1:
        return True
    q1 = deque()
    l1 = len(array)
    i = 1
    q1.append(array[0])
    while i < l1:
        top = q1.popleft()
        if i + 1 >= l1:
            if array[i] < top:
                break
            return False
        if array[i] < top and array[i+1] < top:
            q1.append(array[i])
            q1.append(array[i+1])
            i += 2
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    print(is_max_heap([90, 15, 10, 7, 12, 2, 7, 8]))
