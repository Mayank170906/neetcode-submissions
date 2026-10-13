class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        data = set()
        idx = 0

        for i in s:
            if i in data:
                ans = max(ans, len(data))

                while i in data:
                    data.remove(s[idx])
                    idx += 1

            data.add(i)

        return max(ans, len(data))