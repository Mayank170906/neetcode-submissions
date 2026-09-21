class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        f={0:1}
        s=0
        c=0
        for num in nums:
            s+=num
            need=s-k
            if need in f:
                c+=f[need]
            if s in f:
                f[s]+=1
            else:
                f[s]=1
        return c

