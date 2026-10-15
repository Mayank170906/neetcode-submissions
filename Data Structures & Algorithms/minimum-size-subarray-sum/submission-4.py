class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        idx=0
        ans=0
        ans=len(nums)+1
        for i in range(len(nums)):
            s+=nums[i]
            if s<target:
                continue
            while s-nums[idx]>=target:
                s-=nums[idx]
                idx+=1
            ans=min(ans,i-idx+1)
        return 0 if ans==len(nums)+1 else ans

            