class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        data=sorted(nums)
        c=1
        t=1
        n=len(nums)
        if n==0:
            return 0
        for i in range(1,n):
            if data[i]-data[i-1]==1:
                t+=1
            elif data[i]-data[i-1]==0:
                pass
            else:
                c=max(c,t)
                t=1
        return max(c,t)


        