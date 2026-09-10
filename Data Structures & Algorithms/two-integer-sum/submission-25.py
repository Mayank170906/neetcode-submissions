class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size=len(nums)
        seen={}
        for i in range(size):
            need=target-nums[i]
            if need in seen :
                return [seen[need],i]
            seen[nums[i]]=i