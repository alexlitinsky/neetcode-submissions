class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minH = []

        res = []

        for x, y in points:
            diff = (y ** 2 + x ** 2) ** 1/2
            heapq.heappush(minH, (diff, [x, y]))
        
        while k:
            diff, coords = heapq.heappop(minH)
            res.append(coords)
            k -= 1
        
        return res
        


        