class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k -= 1

        maxH = [-n for n in nums]
        heapq.heapify(maxH)

        while k:
            heapq.heappop(maxH)
            k -= 1
        
        return -maxH[0]

        # 5, 4, 3, 2, 1

        # 1, 1, 2, 3, 4, 5, 5
        