class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ROWS, COLS = len(board), len(board[0])
        rowSet, colSet, diagSet = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".": continue
                n = int(board[r][c])
                if n in rowSet[r] or n in colSet[c] or n in diagSet[(r // 3, c // 3)]:
                    return False
                rowSet[r].add(n)
                colSet[c].add(n)
                diagSet[(r // 3, c // 3)].add(n)

        
        return True

        