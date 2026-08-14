class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}

        def dfs(i, a):
            if (i, a) in cache: return cache[(i, a)]
            if a == 0: return 1
            if a < 0 or i == len(coins): return 0
            
            cache[(i, a)] = 0 
            for j in range(i, len(coins)):
                cache[(i, a)] += dfs(j, a - coins[j])

            return cache[(i, a)]        

        return dfs(0, amount)

        