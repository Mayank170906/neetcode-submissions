class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = sorted(range(len(arr)), key=lambda i: abs(arr[i] - x))
        ans=sorted([arr[idx[i]] for i in range(k)])
        return ans