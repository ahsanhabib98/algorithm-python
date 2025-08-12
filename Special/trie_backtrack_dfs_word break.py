class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            root.addWord(word)
            
        n = len(s)
        visited = set()
        def dfs(i):
            print(visited)
            if i == n:
                return True
            if i in visited:
                return False
            cur = root
            for j in range(i, n):
                c = s[j]
                if c not in cur.children:
                    break
                cur = cur.children[c]
                if cur.isWord:
                    if dfs(j + 1):
                        return True
            visited.add(i)
            return False
        return dfs(0)