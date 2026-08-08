class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=len(nums)
        nums=set(nums)
        return len(nums)!=l