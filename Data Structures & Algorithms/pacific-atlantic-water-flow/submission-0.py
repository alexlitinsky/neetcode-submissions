class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        def bfs(starts):
            q = deque(starts)
            seen = set(starts)
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and 
                        heights[nr][nc] >= heights[r][c] and 
                        (nr, nc) not in seen):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            return seen
        
        pac_start = [(r, 0) for r in range(ROWS)] + [(0, c) for c in range(COLS)]
        atl_start = [(r, COLS - 1) for r in range(ROWS)] + [(ROWS - 1, c) for c in range(COLS)]
       
        pac = bfs(pac_start)
        atl = bfs(atl_start)

        return [list(rc) for rc in pac & atl]


        