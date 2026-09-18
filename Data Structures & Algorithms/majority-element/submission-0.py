class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data=dict()
        for i in nums:
            if i in data:
                data[i]+=1
            else:
                data[i]=1
        ans=-1
        for i in data:
            if data[i]>len(nums)/2:
                return i