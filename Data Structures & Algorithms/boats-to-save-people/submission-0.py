class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i=0
        n=len(people)-1
        c=0
        while i<=n:
            if people[i]+people[n]<=limit:
                c+=1
                i+=1
                n-=1
            else:
                c+=1
                n-=1
        return c