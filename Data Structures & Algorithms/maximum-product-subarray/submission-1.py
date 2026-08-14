class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        
        curMax, curMin = 1, 1

        for n in nums:
            temp = curMax * n 
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp, curMin * n, n)

            res = max(res, curMax)
        
        return res
        


        # 1, 2, -3, 4

        # max 1, 2, -3, 4
        # min 1, 1, -6, -24

        