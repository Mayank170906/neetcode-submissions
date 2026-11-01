class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mx=len(matrix)
        my=len(matrix[0])
        l=0
        r=mx*my-1
        while l <= r:
            mid=(l+r) // 2
            mr=mid // my
            mc=mid % my
            if matrix[mr][mc] == target:
                return True
            if matrix[mr][mc] > target:
                r=mid-1
            else:
                l=mid+1
        return False