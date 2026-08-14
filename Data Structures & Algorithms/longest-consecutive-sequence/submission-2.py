class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        res = 1
        setNums = set(nums)

        for n in nums:
            if n - 1 not in setNums:
                cur = 1

                while n + cur in setNums:
                    cur += 1
                    res = max(res, cur)





        return res
        