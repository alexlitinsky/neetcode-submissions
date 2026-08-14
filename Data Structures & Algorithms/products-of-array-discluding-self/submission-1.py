class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr = nums[:]
        pre = 1
        for i in range(len(nums)):
            tmp = nums[i]
            arr[i] = pre
            pre *= tmp
        
        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            tmp = nums[i]
            arr[i] *= suf
            suf *= tmp
        
        return arr



        # [1, 2, 4, 6]

        # pre = 1
        # [1, 1, 2, 8]

        # [48   24, 12 , 8]
        