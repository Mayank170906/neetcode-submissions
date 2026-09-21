class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        t=1
        while t in nums:
            t+=1
        return t

        