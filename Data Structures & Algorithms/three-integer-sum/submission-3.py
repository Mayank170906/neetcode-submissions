class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=set()
        if n<3:
            return ans
        for i in range(2,n):
            target=-nums[i]
            s=dict()
            for j in range(i):
                find=target-nums[j]
                if find in s:
                    ans.add(tuple(sorted([find,nums[j],nums[i]])))
                s[nums[j]]=True
        return [list(i) for i in ans]