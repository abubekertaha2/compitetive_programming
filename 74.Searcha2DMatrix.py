class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            r, c = mid // n, mid % n
            value = matrix[r][c]
            if value == target:
                return True
            elif value < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
