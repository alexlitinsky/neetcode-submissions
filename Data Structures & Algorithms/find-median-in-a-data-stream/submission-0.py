class MedianFinder:

    def __init__(self):
        self.minRight, self.maxLeft = [], []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxLeft, -num)

        val = -heapq.heappop(self.maxLeft)
        heapq.heappush(self.minRight, val)
        if len(self.minRight) > len(self.maxLeft):
            val = heapq.heappop(self.minRight)
            heapq.heappush(self.maxLeft, -val)
        

    def findMedian(self) -> float:
        if len(self.maxLeft) > len(self.minRight):
            return -1 * self.maxLeft[0]
        return (-self.maxLeft[0] + self.minRight[0]) / 2
        


        