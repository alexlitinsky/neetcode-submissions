class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        rob1, rob2 = 0, 0 

        for n in nums:
            newRob = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = newRob
        
        return rob2

        # 1  1 3 3

        # r1 r2. 4

        # rob1, rob2 = 10, 12

        # 2   9   8  3  6
        