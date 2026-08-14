class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0

        seq = set(nums)

        for n in nums:
            if n - 1 not in seq:
                tmp = n
                L = 1
                while tmp in seq:
                    res = max(res, L)
                    tmp += 1
                    L += 1



        return res
        