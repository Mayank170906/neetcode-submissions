class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        def split(s,nums,k):
            cnt=1
            temp=s
            for i in nums:
                if temp<i:
                    cnt+=1
                    temp=s-i
                else:
                    temp-=i
            return cnt<=k
        while l<r:
            mid=(l+r)//2
            if split(mid,nums,k):
                r=mid
            else:
                l=mid+1
        return r
        