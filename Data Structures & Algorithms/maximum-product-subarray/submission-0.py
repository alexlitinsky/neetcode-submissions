class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_so_far = min_so_far = res = nums[0]

        for n in nums[1:]:
            if n < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            max_so_far = max(n, max_so_far * n)
            min_so_far = min(n, min_so_far * n)

            res = max(res, max_so_far)

        return res
        


        # 1, 2, -3, 4

        # max 1, 2, 
        # min 1, 1

        