import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=""
        for i in strs:
            ans+=str(len(i))+str("#")
            ans+=str(i)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
    
        while i < len(s):
            j = s.index("#", i)
            size = int(s[i:j])
            i = j + 1
    
            ans.append(s[i:i + size])
            i += size
    
        return ans



