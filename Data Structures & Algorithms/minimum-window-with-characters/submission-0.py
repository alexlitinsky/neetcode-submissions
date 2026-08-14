class Solution:
    def minWindow(self, s: str, t: str) -> str:

        goalSet = Counter(t)
        charSet = defaultdict(int)
        res = [-1, -1]
        L = float('inf')
        have, need = 0, len(goalSet)

        l = r = 0

        while r < len(s):
            charSet[s[r]] += 1 
            if s[r] in goalSet and charSet[s[r]] == goalSet[s[r]]:
                have += 1
            r += 1

            while have == need:
                if r - l < L:
                    res = [l, r]
                    L = r - l
                charSet[s[l]] -= 1
                if s[l] in goalSet and charSet[s[l]] < goalSet[s[l]]:
                    have -= 1
                l += 1
            
        return s[res[0] : res[1]] if L != float('inf') else ""