import bisect
from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.m = defaultdict(SortedDict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""

        timestamps = self.m[key]
        idx = timestamps.keys()
        i = bisect.bisect_right(idx,timestamp)-1
        if i >= 0:
            v = idx[i]
            return self.m[key][v]
        return ""
        
