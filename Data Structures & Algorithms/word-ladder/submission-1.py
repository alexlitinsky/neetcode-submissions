class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
       
        adj = defaultdict(list)
        L = len(beginWord)
        words = set(wordList)
        words.add(beginWord)

        for w in words:
            for i in range(L):
                adj[w[:i] + "*" + w[i + 1:]].append(w)
        
        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while q:
            word, steps = q.popleft()
            for i in range(L):
                pat = word[:i] + "*" + word[i + 1:]
                for nei in adj[pat]:
                    if nei == endWord:
                        return steps + 1
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, steps + 1))
                adj[pat].clear()
        return 0

        