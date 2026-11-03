from bisect import bisect_right,bisect_left
class TimeMap:

    def __init__(self):
        self.data=dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key][timestamp]=value
        else:
            self.data[key]=dict()
            self.data[key][timestamp]=value


    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            ts=list(self.data[key].keys())
            idx=bisect_right(ts,timestamp)-1
            return self.data[key][ts[idx]] if idx>=0 else ''
        else:
            return ''
        
