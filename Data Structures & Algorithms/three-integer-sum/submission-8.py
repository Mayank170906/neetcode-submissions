class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=set()
        nums.sort()
        if n<3:
            return []
        for i in range(2,n):
            target=-nums[i]
            s=set()
            for j in range(i):
                find=target-nums[j]
                if find in s:
                    ans.add(tuple([find,nums[j],nums[i]]))
                s.add(nums[j])
        return [list(i) for i in ans]