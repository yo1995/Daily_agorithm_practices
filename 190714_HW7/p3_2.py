def rain_drop(drops):

    accu = 10000

    covered = [i for i in range(accu + 1)]
    count = 0
    for d in drops:
        count += 1
        for i in range(int(d[0] * accu), int(d[1] * accu + 1)):
            covered[i] = -1
        t = 0
        for i in covered:
            if i != -1:
                t += 1
        if t == 0:
            return count
    return -1


if __name__ == '__main__':
    rains = [[0, 0.3], [0.3, 0.6], [0.5, 0.8], [0.67, 1], [0, 0.4], [0.5, 0.75]]
    print(rain_drop(rains))
