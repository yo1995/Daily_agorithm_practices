from Queue import PriorityQueue


def merge_k_sorted_arrays(lists):
    q = PriorityQueue()
    results = []
    for l in lists:
        for val in l:
            q.put(val)
    while q.qsize() > 0:
        results.append(q.get())
    return results

