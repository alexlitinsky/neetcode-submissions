class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        minH = [(0, 0)]
        total = 0

        while len(visited) < n:
            cost, i = heapq.heappop(minH)
            if i in visited: continue
            total += cost
            visited.add(i)
            for j in range(n):
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(minH, (dist, j))
        


        return total
        