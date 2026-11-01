class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        r=x//2
        l=1
        while l<=r:
            mid=(l+r)//2
            data=mid*mid
            if data==x:
                return mid
            if data<x:
                l=mid+1
            else:
                r=mid-1
        
        return r