class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        r, c = M-1, 0
        
        while r >= 0 and c < N:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                c += 1
            else:
                r -= 1
        return False