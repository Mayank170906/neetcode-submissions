class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        for i in range(n):
            j=1
            while i+j<n and j<=k:
                if nums[i]==nums[i+j]:
                    return True
                j+=1
        return False


        