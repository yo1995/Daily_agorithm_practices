def my_counter(elements):
    c = {}
    for n in elements:
        c[n] = c.get(n, 0) + 1
    return c
