arr = [1, 3, 2, 4, 5, 6]
# 1 6 2 5 3 4


def sol(a):
    temp_a = sorted(a).copy()
    j = len(a) - 1
    for i in range(len(a)):
        print(int(i / 2))
        if i % 2 == 0:
            a[i] = temp_a[int(i / 2)]
        else:
            a[i] = temp_a[j - int(i / 2)]
    return a


print(sol(arr))