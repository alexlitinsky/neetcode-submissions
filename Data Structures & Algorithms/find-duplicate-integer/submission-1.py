class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n1, n2 = nums[0], nums[nums[0]]

        while n1 != n2:
            n1 = nums[n1]
            n2 = nums[nums[n2]]
        
        n1 = 0

        while n1 != n2:
            n1 = nums[n1]
            n2 = nums[n2]
        
        return n1



        