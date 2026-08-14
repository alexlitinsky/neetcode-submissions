class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]


        # 0, 1, 2, 3, 4, 5
        # 3, 4, 5, 6, 1, 2

        #.L        L  M   R


        # 4, 5, 0, 1, 2, 3
        # L.    M        R

        # 4, 5, 6, 7, 8, 9
        # L.    M.       R
        