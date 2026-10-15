class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        data=dict()
        ans=0
        l=0
        mf=0
        for r in range(len(s)):
            ch=s[r]
            data[ch]=data.get(ch,0)+1
            mf=max(mf,data[ch])
            while (r-l+1-mf)>k:
                data[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans