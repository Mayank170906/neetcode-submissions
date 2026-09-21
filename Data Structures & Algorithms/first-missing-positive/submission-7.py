class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        t=1
        nums=sorted(set(nums))
        while t in nums:
            t+=1
        return t

        