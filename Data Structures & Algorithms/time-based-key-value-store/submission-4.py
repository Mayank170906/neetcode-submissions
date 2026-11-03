from bisect import bisect_right,bisect_left
class TimeMap:

    def __init__(self):
        self.data=dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key][0][timestamp]=value
            self.data[key][1].append(timestamp)
        else:
            self.data[key]=(dict(),list())
            self.data[key][0][timestamp]=value
            self.data[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ''
        d,ts=self.data[key]
        idx=bisect_right(ts,timestamp)-1
        return d[ts[idx]] if idx >= 0 else ''
        
