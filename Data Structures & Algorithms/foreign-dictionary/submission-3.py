class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        charMap = {c:[] for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    charMap[w1[j]].append(w2[j])
                    break
        

        res = []
        visit = defaultdict(bool)

        def dfs(i):
            if i in visit: return visit[i]
            visit[i] = False
            for nei in charMap[i]:
                if dfs(nei) == False:
                    return False
            visit[i] = True
            res.append(i)
            return True
        

        for c in list(charMap.keys()):
            if dfs(c) == False:
                return ""

        # return reverse?
        return "".join(res[::-1])



        