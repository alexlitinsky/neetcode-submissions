class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        first, last = nums[:-1], nums[1:]

        # 2 9 3 8 6

        def single_rob(num):
            rob1, rob2 = 0, 0 

            for n in num:
                temp = rob2
                rob2 = max(rob2, n + rob1)
                rob1 = temp
            
            return rob2
        


        return max(single_rob(first), single_rob(last))
        