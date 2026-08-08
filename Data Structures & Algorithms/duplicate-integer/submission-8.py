class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums)==0: return False
        old=nums[0]
        if old==None:
            return False
        for i in nums[1:]:
            new =i
            if(new==old):
                return True
            old=new
        return False