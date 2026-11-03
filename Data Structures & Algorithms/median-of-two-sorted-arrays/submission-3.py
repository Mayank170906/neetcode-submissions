class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        n1,n2=len(nums1),len(nums2)
        n=n1+n2
        l,r=0,n1
        while l<=r:
            i=(l+r)//2
            j=(n+1)//2-i
            al=nums1[i-1] if i>0 else float('-inf')
            ar=nums1[i] if i<n1 else float('inf')
            bl=nums2[j-1] if j>0 else float('-inf')
            br=nums2[j] if j<n2 else float('inf')
            if al>br:
                r=i-1
            elif bl>ar:
                l=i+1
            else:
                maxl=max(al,bl)
                minr=min(ar,br)
                if n%2==1:
                    return maxl
                return (maxl+minr)/2
