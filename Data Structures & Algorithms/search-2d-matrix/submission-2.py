
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r1 = len(matrix)
        r2 = len(matrix[0])

        l = 0
        r = r1 * r2 - 1

        while l <= r:
            mid = (l + r) // 2

            mr = mid // r2
            mc = mid % r2

            if matrix[mr][mc] == target:
                return True

            if matrix[mr][mc] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
