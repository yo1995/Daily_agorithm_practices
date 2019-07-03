
def see_cows(cows):
    # a queue to maintain the current highest cow
    if len(cows) <= 1:
        return 0
    l1 = len(cows)
    stack = [cows[0]]
    count = 0
    for i in range(1, l1):

        if cows[i] < stack[-1] or len(stack) < 1:
            stack.append(cows[i])
        else:
            while len(stack) > 0 and stack[-1] <= cows[i]:
                stack.pop()
                count += len(stack)
            stack.append(cows[i])

    while len(stack) > 0:
        stack.pop()
        count += len(stack)
    return count


if __name__ == '__main__':
    print(see_cows([6,10,3,7,4,12,2]))
