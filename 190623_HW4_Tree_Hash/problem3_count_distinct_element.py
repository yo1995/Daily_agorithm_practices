

def count_distinct_element(array, k):
    if not array:
        return []
    l = len(array)
    if l < k:
        return len(set(l))
    result = []
    for i in range(l - k + 1):
        result.append(len(set(array[i:i+k])))
    return result
