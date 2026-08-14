class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rowSet, colSet = set(), set()

        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowSet.add(r)
                    colSet.add(c)
        
        for r in rowSet:
            matrix[r] = [0] * len(matrix[0])
        
        for c in colSet:
            for i in range(len(matrix)):
                matrix[i][c] = 0
        

        
        