class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.isRoot = False

            def insert(self, word):
                cur = self
                for c in word:
                    if c not in cur.children:
                        cur.children[c] = TrieNode()
                    cur = cur.children[c]
                cur.isRoot = True

            def getRoot(self, word):
                root = ""
                cur = self
                for c in word:
                    if c not in cur.children or cur.isRoot:
                        break
                    root += c
                    cur = cur.children[c]
                return root if cur.isRoot else ""

        trie = TrieNode()
        for word in dictionary:
            trie.insert(word)

        words = sentence.split(" ")
        res = []
        for word in words:
            root = trie.getRoot(word)
            res.append(root) if root else res.append(word)                
        return " ".join(res)