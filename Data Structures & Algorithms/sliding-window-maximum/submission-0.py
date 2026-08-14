class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # [1, 2, 1, 0, 4, 2, 6]
        # 2
        # we 

        res = []

        maxH = []

        for r in range(len(nums)):
            heapq.heappush(maxH, (-nums[r], r))

            while maxH and maxH[0][1] <= r - k:
                heapq.heappop(maxH)
                
            if r >= k - 1:
                res.append(-maxH[0][0])

        return res
        