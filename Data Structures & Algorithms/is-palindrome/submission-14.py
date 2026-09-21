class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=True
        l=0
        r=len(s)-1
        s=s.lower()
        while l<=r:
            if (s[l]<'a' or s[l]>"z") and ((s[l]<"0" or s[l]>"9")):
                l+=1
                continue
            if (s[r]<'a' or s[r]>"z") and ((s[r]<"1" or s[r]>"9")):
                print(1)
                r-=1
                continue       
            
            if (s[r]==s[l]):
                r-=1
                l+=1
                continue
            else:
                ans=False
                return ans
        return True
                    