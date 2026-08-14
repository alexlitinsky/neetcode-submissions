class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = defaultdict(list)

        for word in words:
            for c in word:
                adj[c]

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2: # prefix edge case
                return ""
            minLen = min(len(w1), len(w2))
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break # don't add extra edges

        res = []
        visit = defaultdict(bool)

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = False
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            visit[c] = True
            res.append(c)
            return True
        
        for c in adj:
            if c not in visit:
                if not dfs(c):
                    return ""


        return "".join(res[::-1])
            
        