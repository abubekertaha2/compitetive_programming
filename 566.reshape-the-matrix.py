class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        area = len(mat)*len(mat[0])
        if c * r != area:
            return mat
        else:
            matrix = [[0 for _ in range(c)] for _ in range(r)]
            for i in range(area):
                matrix[i // c][i % c] = mat[i // len(mat[0])][i % len(mat[0])]
        
        return matrix
