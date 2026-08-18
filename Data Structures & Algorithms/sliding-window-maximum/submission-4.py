class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res, l = [], 0
        maxH = [(-nums[i], i) for i in range(k)]
        heapq.heapify(maxH)
        res.append(-maxH[0][0])

        # [-1, 0]
        # k = 1

        for r in range(k, len(nums)):
            l += 1

            while maxH and maxH[0][1] < l:
                heapq.heappop(maxH)
            heapq.heappush(maxH, (-nums[r], r))
            res.append(-maxH[0][0])



        return res

        