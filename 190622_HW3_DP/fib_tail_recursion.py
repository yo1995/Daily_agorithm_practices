

def fib(start, n1, n2) -> int:
    if start == 0:
        return n1
    return fib(start - 1, n2, n1 + n2)

if __name__ == '__main__':
    print(fib(7, 0, 1))

