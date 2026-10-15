class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count=dict()    
        for i in range(len(s1)):
            count[s1[i]]=count.get(s1[i],0)+1
            count[s2[i]]=count.get(s2[i],0)-1
        if all(count[i]==0 for i in count):
            return True
        l=0
        for r in range (len(s1),len(s2)):
            count[s2[r]]=count.get(s2[r],0)-1
            count[s2[l]]=count.get(s2[l],0)+1
            l+=1
            if all(count[i]==0 for i in count):
                return True
        return False
        