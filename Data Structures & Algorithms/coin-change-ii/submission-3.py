class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        cache = {}

        def dfs(i, a):
            if (i, a) in cache: 
                return cache[(i, a)]
            if a == 0: return 1
            if i >= len(coins): return 0

            res = 0
            res += dfs(i + 1, a)

            if a >= coins[i]:
                res += dfs(i, a - coins[i])
            
            cache[(i, a)] = res
            return res

        

        return dfs(0, amount)

        