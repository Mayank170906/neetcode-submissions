from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydata=dict()
        for i in strs:
            counts=Counter(i)
            key = tuple(sorted(Counter(i).items()))
            mydata.setdefault(key,[]).append(i)
        return list(mydata.values())
        