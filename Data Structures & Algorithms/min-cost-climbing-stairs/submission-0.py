class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:]
        n = len(cost)
        i = 2

        while i < len(dp):
            dp[i] += min(dp[i - 1], dp[i - 2])
            i += 1
        
        return min(dp[n - 1], dp[n - 2])



        # [1, 2, 1, 2, 1, 1]

        # [1, 2, 2, 4, 3, 4]
        