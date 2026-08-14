class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}

        def dfs(i, holding):
            if i >= len(prices): return 0 
            key = (i, holding)
            if key in cache: return cache[key]
            
            if holding:
                best = max(prices[i] + dfs(i + 2, not holding), dfs(i + 1, holding))
            else:
                best = max(-prices[i] + dfs(i + 1, not holding), dfs(i + 1, holding))
            
            cache[key] = best

            return best
            
        

        return dfs(0, False)
            