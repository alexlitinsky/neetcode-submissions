class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0

        charSet = defaultdict(int)

        l = 0

        for r in range(len(s)):
            charSet[s[r]] += 1

            while charSet and (r - l + 1 - max(charSet.values()) > k):
                charSet[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)


        return res

        