class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums)<2: return False
        old=nums[0]
        for i in nums[1:]:
            new =i
            if(new==old):
                return True
            old=new
        return False