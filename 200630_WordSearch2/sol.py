class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
            if not node:
                return False
        return node.isWord

class Solution:
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i, j in product(range(len(board)), range(len(board[0]))):
            self.dfs(board, node, i, j, '', res)
        return res
    
    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return 
        board[i][j] = "#"
        for x, y in self.directions:
            self.dfs(board, node, i+x, j+y, path+tmp, res)
        board[i][j] = tmp
