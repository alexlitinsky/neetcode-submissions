class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0

        l = r = 0

        substring = {}

        while r < len(s):
            while s[r] in substring:
                substring[s[l]] -= 1
                if substring[s[l]] <= 0:
                    substring.pop(s[l])
                l += 1

            substring[s[r]] = 1
            res = max(res, r - l + 1)
            r += 1
            



        return res
        