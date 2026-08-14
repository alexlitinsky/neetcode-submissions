class Solution:
    def trap(self, height: List[int]) -> int:
        # maxL
        # maxR
        # height[l]
        # height[r]
        #.         L                 R     
        #height = [0,2,0,3,1,0,1,3,2,1]


        res = 0

        l, r = 0, len(height) - 1

        maxL, maxR = height[0], height[len(height)- 1]

        while l < r:

            if height[l] < height[r]:
                res += min(maxL, maxR) - height[l]
                l += 1
                maxL = max(maxL, height[l])
            else:
                res += min(maxL, maxR) - height[r]
                r -= 1
                maxR = max(maxR, height[r])


        return res
        