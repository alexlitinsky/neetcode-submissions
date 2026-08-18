class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        cur = prices[0]

        for i in range(len(prices)):
            if cur > prices[i]:
                cur = prices[i]
                
            res = max(res, prices[i] - cur)


        return res
        