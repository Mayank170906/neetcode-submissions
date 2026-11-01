class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc=dict()
        for ch in t:
            tc[ch]=tc.get(ch,0)+1
        need=len(tc)
        wc=dict()
        have=0
        ans=[-1,-1]
        anslen=float('inf')
        l=0
        for r in range(len(s)):
            ch=s[r]
            wc[ch]=wc.get(ch,0)+1
            if ch in tc and tc[ch]==wc[ch]:
                have+=1
            while need==have:
                if (r-l+1) < anslen:
                    ans=[l,r]
                    anslen=r-l+1
                wc[s[l]]-=1
                if s[l] in tc and wc[s[l]]<tc[s[l]]:
                    have-=1
                l+=1
        if anslen==float('inf'):
            return ''
        return s[ans[0]:ans[1]+1]