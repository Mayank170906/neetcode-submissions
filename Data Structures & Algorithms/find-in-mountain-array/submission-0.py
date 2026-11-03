class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def peak(mountainArr):
            l=0
            r=mountainArr.length()-1
            while l<r:
                mid=(l+r)//2
                if mountainArr.get(mid)<mountainArr.get(mid+1):
                    l=mid+1
                else:
                    r=mid
            return l
        def sinc(mountainArr,index):
            l=0
            r=index
            while l<=r:
                mid=(l+r)//2
                if mountainArr.get(mid)==target:
                    return mid
                if mountainArr.get(mid)>target:
                    r=mid-1
                else:
                    l=mid+1
            return -1
        def sdec(mountainArr,index):
            l=index
            r=mountainArr.length()-1
            while l<=r:
                mid=(l+r)//2
                if mountainArr.get(mid)==target:
                    return mid
                if mountainArr.get(mid)>target:
                    l=mid+1
                else:
                    r=mid-1
            return -1
        p=peak(mountainArr)
        ans=sinc(mountainArr,p)
        if ans!=-1:
            return ans
        return sdec(mountainArr,p)