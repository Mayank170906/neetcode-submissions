class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        n=len(heights)-1
        ans=-1
        while i<n:
            ans=max(ans,(n-i)*min(heights[i],heights[n]))
            if heights[i]<heights[n]:
                i+=1
            else:
                n-=1
        return ans