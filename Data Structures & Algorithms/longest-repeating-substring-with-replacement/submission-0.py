class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0 
        l = 0

        charSet = defaultdict(int)
        maxValue = 0

        for r in range(len(s)):
            charSet[s[r]] += 1
            maxValue = max(maxValue, charSet[s[r]])
            # replacment
            while r - l - maxValue + 1 > k:
                charSet[s[l]] -= 1
                l += 1


            res = max(res, r - l + 1)


        return res

        # l
        # r
        # maxV
        #     r
        # AAABABB
        #k = 1
        