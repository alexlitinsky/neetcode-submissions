class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums1 = nums[0]
        nums2 = nums[nums[0]]

        while nums1 != nums2:
            nums1 = nums[nums1]
            nums2 = nums[nums[nums2]]


        
        nums1 = 0
        while nums1 != nums2:
            nums1 = nums[nums1]
            nums2 = nums[nums2]
        
        return nums1



        