class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        T = r*c
        if m*n!=T: return mat
        
        output = [[0 for _ in range(c)] for _ in range(r)]
        
        """
        temp = []
        for i in range(m):
            for j in range(n):
                temp.append(mat[i][j])
        
        k = 0
        for i in range(r):
            for j in range(c):
                output[i][j] = temp[k]
                k+=1
        return output
        """
        # Very inefficient due to both loops; O(n^2+n^2) time and O(n+n) space
        k = 0
        for i in range(m):
            for j in range(n):
                output[k//c][k%c] = mat[i][j]
                k+=1
        return output
        
        # Much more efficient; O(n^2) time and O(n) space