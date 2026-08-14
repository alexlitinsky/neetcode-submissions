class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        cache = {}

        def dfs(i, j):
            if i + 1 >= j: return 0
            if (i, j) in cache: return cache[(i, j)]

            best = 0
            for k in range(i + 1, j):
                coins = nums[i] * nums[k] * nums[j]
                best = max(best, dfs(i, k) + coins + dfs(k, j))

            cache[(i, j)] = best

            return best
        
        return dfs(0, len(nums) - 1)


        



        