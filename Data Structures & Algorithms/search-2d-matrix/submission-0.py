class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left, right = 0, len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                innerLeft, innerRight = 0, len(matrix[0]) - 1
                while innerLeft <= innerRight:
                    innerMid = (innerLeft + innerRight) // 2
                    if target == matrix[mid][innerMid]: return True
                    elif target < matrix[mid][innerMid]:
                        innerRight = innerMid - 1
                    else:
                        innerLeft = innerMid + 1
                return False
            elif target < matrix[mid][0] and target < matrix[mid][-1]:
                right = mid - 1
            else:
                left = mid + 1 

        return False
        