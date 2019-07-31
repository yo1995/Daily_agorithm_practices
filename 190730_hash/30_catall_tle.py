from typing import List


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        if not self.validateWords(words):
            return []
        s1 = set()
        self.generatePerm(words, '', s1)
        l = len(words[0]) * len(words)
        results = []
        for i in range(len(s)):
            if s[i:i+l] in s1:
                results.append(i)
        return results


    def validateWords(self, words: List[str]) -> bool:
        l = len(words[0])
        for i in range(1, len(words)):
            if len(words[i]) != l:
                return False
        return True

    def generatePerm(self, words: List[str], tempStr: str, s: set):
        if not words:
            s.add(tempStr)
            return
        for i in range(len(words)):
            self.generatePerm(words[:i] + words[i + 1:], tempStr + words[i], s)
        return


if __name__ == '__main__':
    s = Solution()

    s1 = "barfoothefoobarman"
    words1 = ["foo", "bar"]

    res = s.findSubstring(s1, words1)
    print(res)
