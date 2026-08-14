class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        res = ""
        maxLen = 0

        def computePali(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r] :
                l -= 1
                r += 1
            
            return s[l + 1:r]

        for i in range(len(s) - 1):
            odd, even = computePali(i, i + 1), computePali(i, i + 2)
            best = max(odd, even, key=len)
            if len(best) > maxLen:
                maxLen, res = len(best), best
        
        return res

        