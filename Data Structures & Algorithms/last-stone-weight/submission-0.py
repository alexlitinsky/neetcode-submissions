class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = [-s for s in stones]
        heapq.heapify(hq)

        while len(hq) > 1:
            l1, l2 = heapq.heappop(hq), heapq.heappop(hq)
            if l1 != l2:
                heapq.heappush(hq, l1 - l2)
        
        return -hq[0] if hq else 0
        