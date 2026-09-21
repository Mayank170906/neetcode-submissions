class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        t=1
        nums.sort()
        while t in nums:
            t+=1
        return t

        