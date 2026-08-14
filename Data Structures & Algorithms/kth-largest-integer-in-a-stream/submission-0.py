class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minH = nums[:]
        heapq.heapify(self.minH)
        self.k = k
        while len(self.minH) > self.k:
            heapq.heappop(self.minH)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minH, val)
        if len(self.minH) > self.k:
            heapq.heappop(self.minH)
        # elif val > self.minH[0]:
        #     heapq.heapreplace(self.minH, val)

        return self.minH[0]
        
