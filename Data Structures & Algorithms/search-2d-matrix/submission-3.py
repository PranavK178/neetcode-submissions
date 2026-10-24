class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = len(matrix[0]) - 1
        r = 0
        while r < len(matrix) and matrix[r][right] < target:
            r += 1
        if r == len(matrix):
            return False
        left = 0
        while left <= right:
            m = (left + right) // 2
            if matrix[r][m] < target:
                left = m + 1
            elif matrix[r][m] > target:
                right = m - 1
            else:
                return True
        return False
        