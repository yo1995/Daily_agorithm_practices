

def find_sub_arrays_On2(array):
    results = []
    l1 = len(array)
    for i in range(l1):
        sum = 0
        for j in range(i, l1):
            sum += array[j]
            if sum == 0:
                results.append((i, j))
    return results


def find_sub_arrays_hash(array):
    sum_dict = dict()
    summation = 0
    results = []
    for i in range(len(array)):
        summation += array[i]
        if summation == 0:
            results.append((0, i))
        if summation in sum_dict:
            for index in sum_dict[summation]:
                results.append((index + 1, i))
            sum_dict[summation].append(i)
            continue
        sum_dict[summation] = [i]
    return sorted(results)


if __name__ == '__main__':
    print(find_sub_arrays_hash([6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]))