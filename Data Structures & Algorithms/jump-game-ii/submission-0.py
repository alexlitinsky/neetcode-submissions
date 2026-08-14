class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        jumps = 0
        curEnd = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == curEnd:
                jumps += 1
                curEnd = farthest
                if curEnd == n - 1:
                    break


        return jumps

        