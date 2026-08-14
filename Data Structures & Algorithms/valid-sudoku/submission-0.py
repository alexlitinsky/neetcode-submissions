class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS, COLS = len(board), len(board[0])

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val == ".": continue
                if (val in cols[c] or
                   val in rows[r] or
                   val in boxes[r // 3][c // 3]):
                   return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[r // 3][c // 3].add(val)

        
        return True
        