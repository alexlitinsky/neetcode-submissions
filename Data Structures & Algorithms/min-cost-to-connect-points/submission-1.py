class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        costs = {(x, y):[] for x, y in points}
        visit = set()
        res = 0

        minH = [(0, points[0][0], points[0][1])]
        while minH and len(visit) != len(points):
            w, x, y = heapq.heappop(minH)
            if (x, y) in visit: continue
            res += w
            visit.add((x, y))
            for n1, n2 in points:
                if (n1, n2) in visit: continue
                heapq.heappush(minH, (abs(x - n1) + abs(y - n2), n1, n2))
        

        return res





        