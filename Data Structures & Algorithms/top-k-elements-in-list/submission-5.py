class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        data=dict()
        for i in nums:
            if i in data:
                data[i]+=1
            else:
                data[i]=1
        return sorted(data,key=data.get)[-1:-1-k:-1]

            