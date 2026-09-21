class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        t=1
        d=set(nums)
        while t in d:
            t+=1
        return t

        