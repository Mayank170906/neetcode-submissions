class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[1]*n

        p=1
        for i in range(n):
            if i==0:
                continue
            else:
                p*=nums[i-1]
                ans[i]=p

        p=1
        for i in range(n-1,-1,-1):
            if i==n-1:
                continue
            else:
                p*=nums[i+1]
                ans[i]*=p 
        return ans
