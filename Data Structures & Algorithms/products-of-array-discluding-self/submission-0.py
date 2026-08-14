class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [1, 2, 4, 6]
        # prefix = 1

  

        # suffix = 48

        # [1, 24, 12, 8]

        # prefix = 8
        # [1, 1, 2, 8]

        prefix = 1
        res = nums[:]
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res

        