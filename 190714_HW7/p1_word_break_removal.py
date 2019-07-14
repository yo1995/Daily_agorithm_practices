

def word_break(s, words):
    if not s:
        return True
    d = [False] * len(s)
    for i in range(len(s)):
        for w in words:
            if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                d[i] = True
    return d[-1]


def remove_characters(s, d):
    if not s:
        return 0
    visited = set()
    result = [len(s), len(s)]
    helper(s, d, result, visited)
    return result[0]


def helper(s, d, res, visited):
    if s not in visited:
        visited.add(s)
        if word_break(s, d):
            res[0] = min(res[0], res[1] - len(s))
            return
    else:
        return
    for i in range(len(s)):
        helper(s[:i]+s[i+1:], d, res, visited)
    return

if __name__ == '__main__':
    s = 'hellowworld'
    d = ['hello', 'world']
    print(remove_characters(s, d))