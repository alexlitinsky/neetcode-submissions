class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        cache = {}
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0
        ROWS, COLS = len(matrix), len(matrix[0])

        def dfs(r, c):
            if (r, c) in cache: return cache[(r, c)]
            best = 1

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))

            cache[(r, c)] = best
            return best


        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))

        return res
        