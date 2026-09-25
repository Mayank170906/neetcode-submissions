class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        if n==0:
            return ans
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            tar=target-nums[i]

            for j in range(i+1,n):
                if nums[j]>0 and nums[j]>tar:
                    break
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l=j+1
                r=n-1
                while l<r:
                    total=nums[l]+nums[r]+nums[j]
                    if total>tar:
                        r-=1
                    elif total<tar:
                        l+=1
                    else:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1     
        return ans               
                    
