from typing import List
from collections import deque
from string import ascii_lowercase

# https://leetcode.com/problems/word-ladder-ii/submissions/
# https://leetcode.com/problems/word-ladder-ii/discuss/40458/Use-defaultdict-for-traceback-and-easy-writing-20-lines-python-code

def get_word_within_1(word_set, word):
    results = set()
    for ii in range(len(word)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if word[ii] == c:
                continue
            new_word = word[:ii] + c + word[ii+1:]
            if new_word in word_set:
                results.add(new_word)
                # word_set.remove(new_word)
    return results


def get_path(paths, pre_list, cur_path, end):
    if end not in pre_list:
        cur_path.append(end)
        cur_path.reverse()
        paths.append(cur_path)
        return
    for p in pre_list[end]:
        new_path = []
        new_path.extend(cur_path)
        new_path.append(end)
        get_path(paths, pre_list, new_path, p)


def update_pre_list(pre_list, cur, pre):

    if cur not in pre_list:
        pre_list[cur] = []
    pre_list[cur].append(pre)


def get_ladder(begin, end, word_list) -> List[List[str]]:
    s = set()
    for w in word_list:
        s.add(w)
    q1 = deque()
    q1.append(begin)

    results = []
    pre_list = dict()

    visited = set()
    visited.add(begin)

    while q1:  # and s:
        q2 = set()
        is_finished = False
        while q1:
            top = q1.popleft()
            l = get_word_within_1(s, top)

            for w in l:
                if end == w:
                    is_finished = True
                if w not in visited:
                    update_pre_list(pre_list, w, top)
                    q2.add(w)

        visited = visited | q2
        if is_finished:
            get_path(results, pre_list, [], end)
            break
        q1.extend(q2)
    return results


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(get_ladder(beginWord, endWord, wordList))
