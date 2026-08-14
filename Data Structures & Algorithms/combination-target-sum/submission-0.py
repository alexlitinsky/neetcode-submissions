class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curr = []

        def backtrack(i):
            total = sum(curr)
            if total >= target or i == len(nums):
                if total == target:
                    res.append(curr[:])
                return
            curr.append(nums[i])
            backtrack(i)
            curr.pop()
            backtrack(i + 1)



        backtrack(0)
        return res
        