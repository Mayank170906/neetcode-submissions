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
            for ts in range(timestamp,-1,-1):
                if ts in self.data[key]:
                    return self.data[key][ts]
        return ''
        
