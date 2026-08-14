class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        half = total // 2
        cache = set()

        for n in nums:
            tmp = cache.copy()
            for t in tmp:
                cache.add(t + n)
            cache.add(n)

        



        return half in cache
        