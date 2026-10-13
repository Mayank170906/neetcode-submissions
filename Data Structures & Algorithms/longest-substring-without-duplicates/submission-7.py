class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        data = set()
        idx = 0
        for i in s:
            while i in data:
                data.remove(s[idx])
                idx+=1
            data.add(i)
            ans=max(ans,len(data))
        return max(ans,len(data))