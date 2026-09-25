class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=set()
        nums.sort()
        if n<3:
            return []
        for i in range(2,n):
            target=-nums[i]
            l=0
            r=i-1
            while l<r:
                if (nums[l]+nums[r])==target:
                    ans.add((nums[l],nums[r],nums[i]))
                    l+=1
                    r-=1
                elif (nums[l]+nums[r])>target:
                    r-=1
                else:
                    l+=1
        return [ list(i) for i in ans]
