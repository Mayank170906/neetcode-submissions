class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        n=len(s)
        i=0
        j=n-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
                continue
            else:
                t1 = s[:i] + s[i+1:] 
                t2 = s[:j] + s[j+1:]
                return t1 == t1[::-1] or t2 == t2[::-1]
        return False