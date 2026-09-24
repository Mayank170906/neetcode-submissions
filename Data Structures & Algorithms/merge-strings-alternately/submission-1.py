class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        n=min(l1,l2)
        ans=""
        for i in range(n):
            ans+=word1[i]+word2[i]
        if (l1==n):
            ans+=word2[n:]
        
        else:
            ans+=word1[n:]
        return ans
        