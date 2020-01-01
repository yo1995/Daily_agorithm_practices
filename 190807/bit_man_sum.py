
def get_sum(a: int, b: int) -> int:
    summation = a
    carry = b
    mask = 0xFFFFFFFF
    MAX = 0x7FFFFFFF
    while carry != 0:
        temp = summation
        summation = (temp ^ carry) & mask
        carry = ((temp & carry) << 1) & mask
    return summation if summation <= MAX else ~(summation ^ mask)


if __name__ == '__main__':
    s = get_sum(-1, 1)
    print('sum', s)
