from typing import List
import random
import time


def insertion_sort(arr: List) -> List[int]:
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr


def selection_sort(arr: List) -> List[int]:
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def generate_random_array(low: int, high: int, length: int):
    return [random.randint(low, high) for _ in range(length)]


def generate_nearly_sorted_array(low: int, high: int, swap_count: int) -> List[int]:
    arr = [i for i in range(low, high, 1)]
    for i in range(swap_count):
        x = random.randint(low, high-1) - low
        y = random.randint(low, high-1) - low
        arr[x], arr[y] = arr[y], arr[x]
    return arr


if __name__ == '__main__':
    lo = 0
    hi = 10000
    count = 10000
    # a = generate_random_array(lo, hi, count)
    a = generate_nearly_sorted_array(lo, hi, 10)
    b = a.copy()
    c = a.copy()
    
    t = time.time()
    c.sort()
    print('tim_sort', time.time() - t)
    t = time.time()
    a = insertion_sort(a)
    print('insertion_sort', time.time() - t)
    t = time.time()
    b = selection_sort(b)
    print('selection_sort', time.time() - t)
    if a != b or a != c or b != c:
        print('wrong')
