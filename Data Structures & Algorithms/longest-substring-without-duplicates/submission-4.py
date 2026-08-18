class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        l = 0
        charSet = defaultdict(int)

        for r in range(len(s)):
            while s[r] in charSet:
                charSet[s[l]] -= 1
                if charSet[s[l]] == 0:
                    del charSet[s[l]]
                l += 1
                
            charSet[s[r]] += 1
            res = max(res, r - l + 1)





        return res
        