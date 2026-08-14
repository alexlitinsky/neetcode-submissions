class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

            
        l, r = 0, 0
        jumps = 0
        farthest = 0

        while r < len(nums):
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            jumps += 1
            if r == len(nums) - 1: 
                break


        return jumps

        