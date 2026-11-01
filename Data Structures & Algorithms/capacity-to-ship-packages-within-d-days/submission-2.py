class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<=r:
            mid=(l+r)//2
            day=1
            wgt=mid
            for i in weights:
                if wgt<i:
                    wgt=mid
                    day+=1
                wgt-=i
            if day<=days:
                r=mid-1
            else:
                l=mid+1
        return l
            
