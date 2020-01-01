import math

# Project Euler 108


def factor_count_standard(n2: int):
    count = 2  # 1 and num itself
    results = [1, n2]
    root = int(math.sqrt(n2))  # n^2 is guaranteed to be sqrt-able
    for i in range(2, root + 1):
        if n2 % i == 0:
            if i == root and n2 / i == i:
                count += 1
                results.append(i)
            else:
                count += 2
                results.append(i)
                results.append(n2/i)
    return count, results


def factor_count(n2: int):
    count = 1  # 1
    results = [1]
    root = int(math.sqrt(n2))  # n^2 is guaranteed to be sqrt-able
    for i in range(2, root + 1):
        if n2 % i == 0:
            count += 1
            results.append(i)
    return count, results


def prime_factors(n: int):
    results = []
    while n % 2 == 0:
        results.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            results.append(i)
            n = n // i
    if n > 2:
        results.append(n)
    return results


def construct_solutions(n, factors, pairs):
    for e in factors:
        x = e + n
        y = n * n // e + n
        pairs.append((x, y))
    return


def main():
    result_pairs = []

    max_n = 0
    max_count = 0
    max_factors = []
    for n in range(180100, 180180):
        count, factors = factor_count(n * n)
        # if count == 20:
        #     max_n = n
        #     max_count = count
        #     max_factors = factors
        #     print(factors)
        #     break
        if count > max_count:
            max_n = n
            max_count = count
            max_factors = factors
    construct_solutions(max_n, max_factors, result_pairs)
    return max_n, max_count, result_pairs


if __name__ == '__main__':
    N, c, res = main()
    print('N =', N)
    print('Results count is:', c)
    print('Solutions:', res)
