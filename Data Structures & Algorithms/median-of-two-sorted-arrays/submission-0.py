class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans=sorted(nums1+nums2)
        n=len(ans)
        if n%2!=0:
            return ans[int(n/2)]
        return (ans[int(n/2)]+ans[int(n/2)-1])/2
        