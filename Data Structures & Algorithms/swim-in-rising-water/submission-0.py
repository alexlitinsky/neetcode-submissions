class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        time = 0
        visit = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visit = set((0, 0))
        minH = [(grid[0][0], 0, 0)]
        res = 0

        while minH:
            time, r, c = heapq.heappop(minH)
            res = max(res, time)
            if r == n - 1 and c == n - 1: 
                return res
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr and nr < n and 0 <= nc and nc < n and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(minH, (grid[nr][nc], nr, nc))
        