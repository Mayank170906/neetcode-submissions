class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count=0 
        words=min(strs,key=len)
        size=len(words)
        for i in range(size):
            for j in range(len(strs)):
                if (strs[j][i]==words[i]):
                    pass
                else:
                    return strs[0][0:count]
            count+=1
        return strs[0][0:count]
