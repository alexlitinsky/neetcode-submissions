class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.endWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root

        def innerSearch(word, node):
            if not word:
                return node.endWord
            
            if word[0] == ".":
                val = False
                for n in node.children.values():
                    val |= innerSearch(word[1:], n)
                return val
            elif word[0] in node.children:
                return innerSearch(word[1:], node.children[word[0]])
            else:
                return False

        
        return innerSearch(word, curr)
            
        
