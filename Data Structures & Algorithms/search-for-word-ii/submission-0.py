class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endWord = True
    

    def search(self, word):
        curr = self.root

        for c in word:
            if c not in word:
                return False
            curr = curr.children[c]
        
        return curr.endWord
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        res = set()

        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        def dfs(r, c, node, word):
            nonlocal res
            if (r < 0 or r >= ROWS or c < 0 or
                c >= COLS or (r, c) in visited or board[r][c] not in node.children):
                return
            
            char = board[r][c]
            word += char
            node = node.children[char]
            visited.add((r, c))

            if node.endWord:
                res.add(word)

            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))
            
        

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie.root, "")

        return list(res)

        