class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # 2 x 2, 3 x 3, 4 x 4
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                # save topLeft
                topLeft = matrix[top][l + i]

                # bottomLeft to topLeft
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # bottomRight ot bottom Left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # topRight to bottomRight
                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft 
            
            l += 1
            r -= 1

        