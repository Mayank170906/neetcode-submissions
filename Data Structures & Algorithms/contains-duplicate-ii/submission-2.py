class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        data=dict()
        for i in range(n):
            if nums[i] in data:
                for j in data[nums[i]]:
                    if abs(i-j)<=k:
                        return True
                data[nums[i]].append(i)
            else:
                data[nums[i]]=[i,] 
        return False



        