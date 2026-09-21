class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        data=dict()
        for i in nums:
            if i in data:
                data[i]+=1
            else:
                data[i]=1
        return [i for i in data if data[i]>len(nums)/3]